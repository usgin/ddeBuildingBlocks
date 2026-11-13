"""Locate a building-block directory by its (pre-reorg) identity name under the group-by-technique
_sources layout.

The reorg renamed the per-technique BB dirs to roles (techniqueProfile/<tech>/{tapp,detail,profile,
profile-ada}), so a lookup by the old identity name (epmaTAPP, detailLAICPMS, adaEPMA, epmaProfile…)
no longer matches a directory name. This resolver maps those names to their new location:

  - identity-named BBs (adaProduct, tappDefinition, registry catalogs, BaseSchema helpers): exact search
  - <x>TAPP        -> techniqueProfile/<tech>/tapp
  - detail<X>      -> techniqueProfile/<tech>/detail   (detailXCT -> .../detail-legacy)
  - ada<X> generic -> techniqueProfile/<tech>/profile-ada
  - <geochem name> -> techniqueProfile/<tech>/profile   (epmaProfile, LA-ICPMS, Geochron, SEM-Imaging…)
"""
from pathlib import Path

# lowercased technique token -> technique directory name under techniqueProfile/
_ALIAS = {
    # "empa" and "empaprofile" are the LEGACY spellings, kept pointing at the renamed directory.
    # _ALIAS is consulted before _tech_scan, and the scan can only find EPMA now, so dropping these
    # would make a lookup by the old token return None -- which per _tech_scan's own note makes the
    # caller "quietly use a laxer schema" rather than fail. 436 stored records still say adaEMPA.
    "empa": "EPMA", "empaprofile": "EPMA",
    "epma": "EPMA", "geochron": "Geochron", "laicpms": "LA-ICPMS", "icpms": "ICPMS",
    "labxct": "XCT", "xct": "XCT", "sem": "SEM", "semimaging": "SEM-Imaging",
    "semfibsem": "SEM-FIBSEM", "semcomposition": "SEM-Composition",
    "solutionqicpms": "Solution-Q-ICPMS", "solutionsficpms": "Solution-SF-ICPMS",
    "tem": "TEM", "argt": "ARGT", "dsc": "DSC", "eairms": "EAIRMS", "icpoes": "ICPOES",
    "l2ms": "L2MS", "laf": "LAF", "nanoir": "NanoIR", "nanosims": "NanoSIMS", "psfd": "PSFD",
    "qris": "QRIS", "sls": "SLS", "vnmir": "VNMIR", "xrd": "XRD", "basemap": "Basemap",
    "aiva": "AIVA", "ams": "AMS", "fticrms": "FTICRMS", "gcms": "GCMS", "gpyc": "GPYC",
    "ic": "IC", "lcms": "LCMS", "lit": "LIT", "ngnsms": "NGNSMS", "raman": "RAMAN",
    "ritofngms": "RITOFNGMS", "sims": "SIMS", "svruec": "SVRUEC", "tofsims": "ToFSIMS",
    "uvfm": "UVFM", "vlm": "VLM", "xanes": "XANES",
    # geochemProfile dir names (path-driven product profiles)
    "epmaprofile": "EPMA", "la-icpms": "LA-ICPMS", "lab-xct": "XCT",
    "sem-imaging": "SEM-Imaging", "sem-fibsem": "SEM-FIBSEM", "sem-composition": "SEM-Composition",
    "solution-q-icpms": "Solution-Q-ICPMS", "solution-sf-icpms": "Solution-SF-ICPMS",
}


def _tech(token: str) -> str:
    return _ALIAS.get(token.lower(), token)


def _norm(s: str) -> str:
    return s.replace("-", "").replace("_", "").lower()


def _tech_scan(token: str, tp) -> str | None:
    """The technique directory whose name matches `token` ignoring case and hyphens.

    _ALIAS is a hand-maintained table and it rots: 20 of the technique directories had no entry
    when this was added (every LA-*, Solution-MC-ICPMS, CAPD, TIMS, S-XRF and the rest), so a
    lookup for e.g. adaSolutionMCICPMS fell through to None and its caller quietly used a laxer
    schema. Scanning the directories themselves cannot fall behind them. _ALIAS is still consulted
    first, since it also encodes deliberate REDIRECTS (basemap -> Basemap, epmaprofile -> EPMA)
    that are not simple spelling differences.
    """
    want = _norm(token)
    for root in ("geochemProfile", "adaProfile"):
        d = tp / root
        if not d.is_dir():
            continue
        for cand in d.iterdir():
            if cand.is_dir() and _norm(cand.name) == want:
                return cand.name
    return None


def find_bb_dir(name: str, sources) -> Path | None:
    """Return the BB directory for `name` under `sources` (the _sources root), or None."""
    sources = Path(sources)
    tp = sources / "techniqueProfile"

    def ok(d: Path):
        return d if d.is_dir() and (d / "schema.yaml").exists() else None

    def at(tech: str, role: str):
        """Technique dirs sit under one of two roots: geochemProfile (TAPP-aware) or adaProfile.
        Trying both keeps the locator working if a technique later moves between them."""
        for root in ("geochemProfile", "adaProfile"):
            if (hit := ok(tp / root / tech / role)):
                return hit
        scanned = _tech_scan(tech, tp)
        if scanned and scanned != tech:
            for root in ("geochemProfile", "adaProfile"):
                if (hit := ok(tp / root / scanned / role)):
                    return hit
        return None

    # 1. identity-named BB anywhere (adaProduct, tappDefinition, registry catalogs, BaseSchema helpers)
    for cand in sources.rglob(name):
        if (hit := ok(cand)):
            return hit
    # 2. <x>TAPP
    if name.endswith("TAPP"):
        if (hit := at(_tech(name[:-4]), "tapp")):
            return hit
    # 3. detail<X>  (old detailXCT stub lives under detail-legacy)
    if name.startswith("detail"):
        role = "detail-legacy" if name == "detailXCT" else "detail"
        if (hit := at(_tech(name[len("detail"):]), role)):
            return hit
    # 4. generic ada<X> profile
    if name.startswith("ada"):
        tech = _tech(name[3:])
        if (hit := at(tech, "profile-ada")):
            return hit
        # A technique may publish its ada<X> name from the PATH-DRIVEN profile/ instead of a
        # generic profile-ada/ -- the three Solution ICP-MS techniques do. Without this fallback
        # adaSolutionQICPMS, adaSolutionSFICPMS and adaSolutionMCICPMS all resolved to None, so
        # validate_instance fell back to the default adaProduct and every solution-specific
        # constraint went unenforced -- silently, since a record that validates against a laxer
        # schema still passes. Measured on exampleadaSolutionMCICPMS-ETHZ-20240903.json, which
        # names adaSolutionMCICPMS in dcterms:conformsTo and was being checked against adaProduct.
        if (hit := at(tech, "profile")):
            return hit
    # 5. path-driven geochem product profile (by dir/technique name)
    if (hit := at(_tech(name), "profile")):
        return hit
    return None

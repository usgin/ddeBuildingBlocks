"""Add resolvedSchema URLs to register.json for all building blocks."""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTER = REPO_ROOT / "build" / "register.json"
SOURCES = REPO_ROOT / "_sources"

# Prefix to strip from itemIdentifier to get the relative source path.
# e.g. dde.bbr.metadata.profiles.DDEProfiles.DDEDiscovery -> profiles/DDEProfiles/DDEDiscovery
#      dde.bbr.metadata.DDEproperties.ddeCore -> DDEproperties/ddeCore
ID_PREFIX = "dde.bbr.metadata."


def main():
    with open(REGISTER) as f:
        register = json.load(f)

    base_url = register.get("baseURL", "").rstrip("/")
    count = 0

    for bblock in register.get("bblocks", []):
        item_id = bblock.get("itemIdentifier", "")
        if not item_id.startswith(ID_PREFIX):
            continue

        # Convert dotted suffix to path: DDEproperties.ddeCore -> DDEproperties/ddeCore
        rel = item_id[len(ID_PREFIX):].replace(".", "/")
        resolved_path = SOURCES / rel / "resolvedSchema.json"

        if resolved_path.exists():
            url = f"{base_url}/_sources/{rel}/resolvedSchema.json"
            bblock["resolvedSchema"] = url
            count += 1

    with open(REGISTER, "w") as f:
        json.dump(register, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added resolvedSchema to {count} building blocks.")


if __name__ == "__main__":
    main()

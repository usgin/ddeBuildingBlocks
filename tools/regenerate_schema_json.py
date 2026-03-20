#!/usr/bin/env python3
# regenerate_schema_json.py — canonical copy lives in metadataBuildingBlocks/tools/
# Sync to domain repos via: python tools/sync_resolve_schema.py
# VERSION: 2026-03-20
"""Regenerate *Schema.json files from schema.yaml sources.

For each building block that has a schema.yaml, this script:
1. Reads the YAML source
2. Converts to JSON
3. Rewrites $ref paths from schema.yaml → {blockName}Schema.json
4. Writes the output *Schema.json file

The schema.yaml is the source of truth. This script ensures
*Schema.json files stay in sync.
"""

import json
import os
import re
import sys
import yaml

SOURCES_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__), '..', '_sources'
))

# Special naming overrides (dir_name -> Schema.json filename)
NAME_OVERRIDES = {
    'cdifVariableMeasured': 'cdiVariableMeasuredSchema.json',
}


def get_schema_json_name(dir_name):
    """Get the *Schema.json filename for a given directory name."""
    if dir_name in NAME_OVERRIDES:
        return NAME_OVERRIDES[dir_name]
    return f'{dir_name}Schema.json'


def build_dir_to_name_map(sources_dir):
    """Build a mapping from directory path to Schema.json filename."""
    mapping = {}
    for root, dirs, files in os.walk(sources_dir):
        if 'schema.yaml' in files:
            dir_name = os.path.basename(root)
            mapping[dir_name] = get_schema_json_name(dir_name)
    return mapping


def rewrite_ref(ref_value, dir_name_map):
    """Rewrite a $ref value from schema.yaml to *Schema.json path.

    Examples:
        ../definedTerm/schema.yaml -> ../definedTerm/definedTermSchema.json
        ../../schemaorgProperties/person/schema.yaml -> ../../schemaorgProperties/person/personSchema.json
    """
    if not ref_value.endswith('/schema.yaml'):
        return ref_value

    # Extract the directory name from the path
    parts = ref_value.rsplit('/', 2)
    if len(parts) >= 2:
        dir_name = parts[-2]
        prefix = '/'.join(parts[:-1])
        json_name = dir_name_map.get(dir_name, f'{dir_name}Schema.json')
        return f'{prefix}/{json_name}'

    return ref_value


def walk_and_rewrite_refs(obj, dir_name_map):
    """Recursively walk a JSON structure and rewrite $ref values."""
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if key == '$ref' and isinstance(value, str):
                result[key] = rewrite_ref(value, dir_name_map)
            else:
                result[key] = walk_and_rewrite_refs(value, dir_name_map)
        return result
    elif isinstance(obj, list):
        return [walk_and_rewrite_refs(item, dir_name_map) for item in obj]
    else:
        return obj


def process_building_block(yaml_path, dir_name_map, dry_run=False):
    """Process a single building block: read YAML, write JSON."""
    dir_path = os.path.dirname(yaml_path)
    dir_name = os.path.basename(dir_path)
    json_name = get_schema_json_name(dir_name)
    json_path = os.path.join(dir_path, json_name)

    # Read YAML
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if data is None:
        print(f'  SKIP {dir_name}: empty schema.yaml')
        return None

    # Rewrite $ref paths
    data = walk_and_rewrite_refs(data, dir_name_map)

    if dry_run:
        print(f'  DRY RUN: {dir_name}/schema.yaml -> {json_name}')
        return json_path

    # Write JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')

    return json_path


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '-v' in sys.argv or '--verbose' in sys.argv

    # Build directory name mapping
    dir_name_map = build_dir_to_name_map(SOURCES_DIR)

    if verbose:
        print(f'Found {len(dir_name_map)} building blocks with schema.yaml')
        print()

    # Find and process all schema.yaml files
    processed = []
    created = []
    updated = []

    for root, dirs, files in sorted(os.walk(SOURCES_DIR)):
        if 'schema.yaml' not in files:
            continue

        yaml_path = os.path.join(root, 'schema.yaml')
        dir_name = os.path.basename(root)
        json_name = get_schema_json_name(dir_name)
        json_path = os.path.join(root, json_name)

        is_new = not os.path.exists(json_path)

        rel_path = os.path.relpath(root, SOURCES_DIR)

        result = process_building_block(yaml_path, dir_name_map, dry_run=dry_run)

        if result:
            processed.append(rel_path)
            if is_new:
                created.append(f'{rel_path}/{json_name}')
                status = 'CREATED'
            else:
                updated.append(f'{rel_path}/{json_name}')
                status = 'UPDATED'

            if verbose:
                print(f'  {status}: {rel_path}/{json_name}')

    print(f'\nProcessed {len(processed)} building blocks')
    if created:
        print(f'  Created: {len(created)} new files')
        for f in created:
            print(f'    + {f}')
    if updated:
        print(f'  Updated: {len(updated)} existing files')


if __name__ == '__main__':
    main()

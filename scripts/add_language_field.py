#!/usr/bin/env python3
"""
Add 'language' field to all metadata.json files.
This script adds "language": "python" after the "jtbd" field.
"""

import json
from pathlib import Path


def add_language_field(metadata_path: Path):
    """Add language field to metadata.json"""
    with open(metadata_path, 'r') as f:
        data = json.load(f)

    # Check if language field already exists
    if 'language' in data:
        print(f"  ✓ {metadata_path.parent.name} (already has language field)")
        return False

    # Add language field after jtbd
    # We'll rebuild the dict in the correct order
    new_data = {}
    for key, value in data.items():
        new_data[key] = value
        if key == 'jtbd':
            new_data['language'] = 'python'

    # Write back with proper formatting
    with open(metadata_path, 'w') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add newline at end

    print(f"  ✓ {metadata_path.parent.name} (added language: python)")
    return True


def main():
    """Main entry point"""
    script_dir = Path(__file__).parent
    examples_dir = script_dir.parent / 'examples'

    print("Adding 'language' field to all metadata.json files...\n")

    # Find all metadata.json files
    metadata_files = list(examples_dir.glob('*/*/metadata.json'))

    updated_count = 0
    skipped_count = 0

    for metadata_path in sorted(metadata_files):
        if add_language_field(metadata_path):
            updated_count += 1
        else:
            skipped_count += 1

    print(f"\n✅ Complete!")
    print(f"   Updated: {updated_count}")
    print(f"   Skipped: {skipped_count}")
    print(f"   Total: {len(metadata_files)}")


if __name__ == "__main__":
    main()

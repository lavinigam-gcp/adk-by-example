#!/usr/bin/env python3
"""
Generate examples.json for the website from all example metadata.

This script scans all examples and creates a JSON file that the website
can use to dynamically display all available examples.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


def load_example_metadata(example_path: Path) -> Dict[str, Any]:
    """Load metadata for a single example"""
    metadata_file = example_path / 'metadata.json'

    if not metadata_file.exists():
        return None

    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        # Add the path information
        category = example_path.parent.name
        metadata['category'] = category
        metadata['category_name'] = category_to_name(category)
        metadata['path'] = f"{category}/{example_path.name}"
        metadata['github_url'] = f"https://github.com/lavinigam-gcp/adk-by-example/tree/main/examples/{category}/{example_path.name}"
        metadata['command'] = f"adk web # Select '{example_path.name.replace('-', '_')}'"

        # Ensure tech_stack field exists (even if empty) for consistent schema
        if 'tech_stack' not in metadata:
            metadata['tech_stack'] = []

        # Ensure status field exists (default to 'ready')
        if 'status' not in metadata:
            metadata['status'] = 'ready'

        return metadata
    except Exception as e:
        print(f"Warning: Could not load metadata for {example_path}: {e}")
        return None


def category_to_name(category: str) -> str:
    """Convert category folder name to display name"""
    category_names = {
        '01-getting-started': 'Getting Started',
        '02-connecting-llms': 'Connecting to LLMs',
        '03-adding-capabilities': 'Adding Capabilities',
        '04-orchestrating-agents': 'Orchestrating Agents',
        '05-managing-context': 'Managing State & Context',
        '06-going-production': 'Going to Production',
        '07-advanced-patterns': 'Advanced Patterns'
    }
    return category_names.get(category, category.replace('-', ' ').title())


def generate_examples_json():
    """Generate the examples.json file for the website"""

    # Find the examples directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    examples_dir = project_root / 'examples'
    website_dir = project_root / 'website'

    if not examples_dir.exists():
        print(f"Error: Examples directory not found at {examples_dir}")
        return False

    # Create website directory if it doesn't exist
    website_dir.mkdir(exist_ok=True)

    # Collect all examples
    all_examples = []
    examples_by_category = {}

    # Get all category directories
    categories = sorted([d for d in examples_dir.iterdir()
                        if d.is_dir() and not d.name.startswith('_')])

    for category_dir in categories:
        category_name = category_to_name(category_dir.name)
        examples_by_category[category_name] = []

        # Get all example directories in this category
        examples = sorted([d for d in category_dir.iterdir() if d.is_dir()])

        for example_dir in examples:
            metadata = load_example_metadata(example_dir)
            if metadata:
                all_examples.append(metadata)
                examples_by_category[category_name].append(metadata)

    # Remove empty categories
    examples_by_category = {k: v for k, v in examples_by_category.items() if v}

    # Create the output structure
    output = {
        'version': '1.0',
        'total_examples': len(all_examples),
        'categories': list(examples_by_category.keys()),
        'examples': all_examples,
        'examples_by_category': examples_by_category
    }

    # Write to website directory
    output_file = website_dir / 'examples.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"✅ Generated examples.json with {len(all_examples)} examples")
    print(f"   Categories: {', '.join(examples_by_category.keys())}")
    print(f"   Output: {output_file}")

    # Also create a simplified version for the website
    simple_output = {}
    for category_name, examples in examples_by_category.items():
        simple_output[category_name] = [
            {
                'title': ex['title'],
                'jtbd': ex['jtbd'],
                'description': ex['description'],
                'difficulty': ex['difficulty'],
                'path': ex['path'],
                'command': ex['command']
            }
            for ex in examples
        ]

    simple_file = website_dir / 'examples_simple.json'
    with open(simple_file, 'w') as f:
        json.dump(simple_output, f, indent=2)

    return True


def main():
    """Main entry point"""
    success = generate_examples_json()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
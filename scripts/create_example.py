#!/usr/bin/env python3
"""
Scaffold a new ADK example with proper structure and templates.

This script helps contributors quickly create new examples with all the
necessary boilerplate, following the project's best practices.

Usage:
    python scripts/create_example.py \\
        --category "04-orchestrating-agents" \\
        --name "route-to-experts" \\
        --jtbd "When handling diverse requests, I need specialist agents" \\
        --status "coming_soon"
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any


# Category name mappings
CATEGORY_NAMES = {
    '01-getting-started': 'Getting Started',
    '02-connecting-llms': 'Connecting to LLMs',
    '03-adding-capabilities': 'Adding Capabilities',
    '04-orchestrating-agents': 'Orchestrating Agents',
    '05-managing-context': 'Managing State & Context',
    '06-going-production': 'Going to Production',
    '07-advanced-patterns': 'Advanced Patterns'
}

# Provider codes
PROVIDERS = ['adk', 'gcp', 'third', 'oss']

# Common tech stack items by category (for quick selection)
COMMON_TECH_STACKS = {
    'adk': {
        'LLM Agent': {'icon': '🤖', 'description': "ADK's intelligent agent with reasoning capabilities"},
        'AgentTool': {'icon': '🔧', 'description': 'Use agents as tools for delegation'},
        'Sequential Agent': {'icon': '➡️', 'description': 'Execute agents in sequence with state passing'},
        'Parallel Agent': {'icon': '⚡', 'description': 'Run multiple agents concurrently'},
        'FunctionTool': {'icon': '🔧', 'description': "ADK's wrapper for exposing functions as agent tools"},
        'Agent Config': {'icon': '📄', 'description': 'YAML-based configuration for no-code agent creation'},
        'GenerateContentConfig': {'icon': '⚙️', 'description': "ADK's configuration system for model parameters"},
        'output_schema': {'icon': '📋', 'description': "ADK's structured output feature for guaranteed JSON format"},
        'ADK CLI': {'icon': '🛠️', 'description': 'Command-line tools for scaffolding and managing ADK projects'},
    },
    'gcp': {
        'Gemini': {'icon': '🔮', 'description': "Google's LLM via AI Studio (free tier available)"},
        'Vertex AI': {'icon': '☁️', 'description': "Google Cloud's enterprise AI platform"},
        'Cloud Run': {'icon': '🚀', 'description': 'Serverless deployment for containerized applications'},
        'Google Search': {'icon': '🔍', 'description': "Google's search API for real-time web information"},
        'BigQuery': {'icon': '📊', 'description': "Google's serverless data warehouse"},
        'Firestore': {'icon': '🗄️', 'description': 'NoSQL document database for state persistence'},
    },
    'oss': {
        'Pydantic': {'icon': '📋', 'description': 'Python data validation using type hints'},
        'Ollama': {'icon': '🦙', 'description': 'Run LLMs locally for offline development'},
    },
    'third': {
        'A2A Protocol': {'icon': '🌐', 'description': 'Agent-to-Agent communication protocol'},
        'Arize': {'icon': '📈', 'description': 'ML observability and monitoring platform'},
    }
}


def create_metadata_template(args: argparse.Namespace) -> Dict[str, Any]:
    """Create metadata.json content from arguments"""

    metadata = {
        "title": args.title or args.name.replace('-', ' ').title(),
        "jtbd": args.jtbd,
    }

    # Add tech_stack if provided
    if args.status == "coming_soon" or args.status == "planned":
        # For placeholder examples, add empty tech_stack to be filled later
        metadata["tech_stack"] = []

    metadata.update({
        "description": args.description or "TODO: Add description",
        "difficulty": args.difficulty,
        "tags": args.tags or [],
        "related": [],
        "source_sample": args.source or "TODO: Link to ADK sample",
        "requirements": ["google-adk"],
        "time_to_complete": args.time,
        "what_youll_learn": [
            "TODO: Add learning point 1",
            "TODO: Add learning point 2",
            "TODO: Add learning point 3"
        ]
    })

    # Add status field if coming_soon or planned
    if args.status in ["coming_soon", "planned"]:
        metadata["status"] = args.status

    # Add priority and sprint for planning
    if args.priority:
        metadata["priority"] = args.priority
    if args.sprint:
        metadata["sprint"] = args.sprint

    return metadata


def create_agent_template(args: argparse.Namespace) -> str:
    """Create agent.py template based on status"""

    if args.status == "coming_soon" or args.status == "planned":
        return f'''"""
{args.title or args.name.replace('-', ' ').title()}

JTBD: {args.jtbd}

Status: {args.status.upper()}
Priority: {args.priority or 'TBD'}
Sprint: {args.sprint or 'TBD'}

TODO: Implement this example
1. Review the metadata.json for requirements
2. Check the ADK sample: {{source_sample}}
3. Implement the agent following ADK best practices
4. Test with `adk web`
5. Update README.md with usage instructions
"""

# TODO: Import necessary ADK components
# from google.adk import Agent, LLMAgent

# TODO: Define your agent
# root_agent = LLMAgent(
#     name="{args.name.replace('-', '_')}",
#     model="gemini-2.5-flash",
#     instructions="TODO: Add agent instructions"
# )
'''
    else:
        return f'''"""
{args.title or args.name.replace('-', ' ').title()}

JTBD: {args.jtbd}
"""

from google.adk import LLMAgent

root_agent = LLMAgent(
    name="{args.name.replace('-', '_')}",
    model="gemini-2.5-flash",
    instructions=\"""
    TODO: Add your agent instructions here.

    Example:
    You are a helpful assistant that helps users with...
    \"""
)
'''


def create_init_template() -> str:
    """Create __init__.py template"""
    return '''"""
Exports the root agent for ADK.
"""

from .agent import root_agent

__all__ = ['root_agent']
'''


def create_readme_template(args: argparse.Namespace, category_name: str) -> str:
    """Create README.md template"""

    status_note = ""
    if args.status in ["coming_soon", "planned"]:
        status_note = f"\n\n> **Status**: 🚧 {args.status.replace('_', ' ').title()} (Priority: {args.priority or 'TBD'}, Sprint: {args.sprint or 'TBD'})\n"

    return f'''# {args.title or args.name.replace('-', ' ').title()}
{status_note}
**Category**: {category_name}
**Difficulty**: {args.difficulty.capitalize()}
**Time to Complete**: {args.time}

## 🎯 Job to Be Done (JTBD)

> {args.jtbd}

## 📖 What You'll Learn

- TODO: Add learning point 1
- TODO: Add learning point 2
- TODO: Add learning point 3

## 🚀 Quick Start

```bash
# From the examples directory
cd examples
adk web

# Select '{args.name.replace('-', '_')}' from the dropdown
```

## 💡 How It Works

TODO: Explain the key concepts and how this example works.

## 🔧 Tech Stack

TODO: List the technologies used (will be auto-populated from metadata.json)

## 📝 Example Usage

TODO: Add example queries or usage patterns

## 🔗 Related Examples

TODO: Link to related examples

## 📚 References

- TODO: Link to ADK sample: {{source_sample}}
- [ADK Documentation](https://github.com/google/adk)

---

**Generated with ADK by Example** - [View all examples](https://lavinigam-gcp.github.io/adk-by-example/)
'''


def create_example(args: argparse.Namespace):
    """Main function to create a new example"""

    # Validate category
    if args.category not in CATEGORY_NAMES:
        print(f"❌ Error: Invalid category '{args.category}'")
        print(f"   Valid categories: {', '.join(CATEGORY_NAMES.keys())}")
        return False

    # Validate status
    valid_statuses = ["ready", "coming_soon", "planned"]
    if args.status not in valid_statuses:
        print(f"❌ Error: Invalid status '{args.status}'")
        print(f"   Valid statuses: {', '.join(valid_statuses)}")
        return False

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    examples_dir = project_root / 'examples'

    # Create example directory path
    category_dir = examples_dir / args.category
    example_dir = category_dir / args.name

    # Check if example already exists
    if example_dir.exists():
        print(f"❌ Error: Example already exists at {example_dir}")
        return False

    # Create category directory if it doesn't exist
    category_dir.mkdir(parents=True, exist_ok=True)

    # Create example directory
    example_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created directory: {example_dir}")

    # Create metadata.json
    metadata = create_metadata_template(args)
    metadata_file = example_dir / 'metadata.json'
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"✅ Created metadata.json")

    # Create agent.py
    agent_content = create_agent_template(args)
    agent_file = example_dir / 'agent.py'
    with open(agent_file, 'w') as f:
        f.write(agent_content)
    print(f"✅ Created agent.py")

    # Create __init__.py
    init_content = create_init_template()
    init_file = example_dir / '__init__.py'
    with open(init_file, 'w') as f:
        f.write(init_content)
    print(f"✅ Created __init__.py")

    # Create README.md
    category_name = CATEGORY_NAMES[args.category]
    readme_content = create_readme_template(args, category_name)
    readme_file = example_dir / 'README.md'
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    print(f"✅ Created README.md")

    print(f"\n🎉 Successfully created example: {args.name}")
    print(f"   Location: {example_dir}")
    print(f"   Status: {args.status}")

    if args.status in ["coming_soon", "planned"]:
        print(f"\n📋 Next Steps:")
        print(f"   1. Update metadata.json with tech_stack")
        print(f"   2. Implement agent.py")
        print(f"   3. Test with: cd examples && adk web")
        print(f"   4. Update status to 'ready' when complete")
    else:
        print(f"\n📋 Next Steps:")
        print(f"   1. Implement agent logic in agent.py")
        print(f"   2. Update metadata.json with accurate details")
        print(f"   3. Complete README.md with examples")
        print(f"   4. Test with: cd examples && adk web")

    print(f"\n🔄 Regenerate website: python scripts/generate_site.py")

    return True


def main():
    """Parse arguments and create example"""
    parser = argparse.ArgumentParser(
        description='Scaffold a new ADK example with proper structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Create a "coming soon" placeholder:
  python scripts/create_example.py \\
      --category "04-orchestrating-agents" \\
      --name "route-to-experts" \\
      --jtbd "When handling diverse requests, I need specialist agents" \\
      --status "coming_soon" \\
      --priority "critical" \\
      --sprint 1

  # Create a ready-to-implement example:
  python scripts/create_example.py \\
      --category "01-getting-started" \\
      --name "my-first-agent" \\
      --title "My First Agent" \\
      --jtbd "When I'm new to ADK, I need a simple example" \\
      --status "ready" \\
      --difficulty "beginner" \\
      --time "5 minutes"

Categories:
  01-getting-started        - Beginner examples
  02-connecting-llms        - Model integrations
  03-adding-capabilities    - Tools and APIs
  04-orchestrating-agents   - Multi-agent patterns
  05-managing-context       - State management
  06-going-production       - Deployment
  07-advanced-patterns      - Complex scenarios
        '''
    )

    parser.add_argument('--category', required=True,
                       help='Category folder (e.g., 04-orchestrating-agents)')
    parser.add_argument('--name', required=True,
                       help='Example name (kebab-case, e.g., route-to-experts)')
    parser.add_argument('--jtbd', required=True,
                       help='Job-to-be-Done statement')
    parser.add_argument('--title',
                       help='Display title (defaults to name in Title Case)')
    parser.add_argument('--description',
                       help='Short description of the example')
    parser.add_argument('--status', default='ready',
                       choices=['ready', 'coming_soon', 'planned'],
                       help='Example status (default: ready)')
    parser.add_argument('--difficulty', default='beginner',
                       choices=['beginner', 'intermediate', 'advanced'],
                       help='Difficulty level (default: beginner)')
    parser.add_argument('--time', default='5 minutes',
                       help='Time to complete (default: 5 minutes)')
    parser.add_argument('--priority',
                       choices=['critical', 'high', 'medium', 'low'],
                       help='Priority for coming_soon examples')
    parser.add_argument('--sprint', type=int,
                       help='Sprint number for coming_soon examples')
    parser.add_argument('--source',
                       help='Source ADK sample name')
    parser.add_argument('--tags', nargs='+',
                       help='Tags for the example')

    args = parser.parse_args()

    # Validate name format (kebab-case)
    if not all(c.islower() or c.isdigit() or c == '-' for c in args.name):
        print("❌ Error: Example name must be in kebab-case (e.g., route-to-experts)")
        return 1

    # Validate priority/sprint for coming_soon
    if args.status == "coming_soon" and not (args.priority and args.sprint):
        print("⚠️  Warning: coming_soon examples should have --priority and --sprint")

    success = create_example(args)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

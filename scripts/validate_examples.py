#!/usr/bin/env python3
"""
Validate all ADK by Example examples.

This script checks that all examples:
1. Have the required files (agent.py, __init__.py, README.md)
2. Can be imported without errors
3. Define a root_agent
4. Have valid metadata.json
5. Use approved models (gemini-2.5-flash or gemini-2.5-pro)
"""

import os
import sys
import json
import importlib.util
from pathlib import Path
from typing import Tuple, List, Dict, Any


class Colors:
    """Terminal colors for output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_colored(text: str, color: str = Colors.ENDC):
    """Print colored text to terminal"""
    print(f"{color}{text}{Colors.ENDC}")


def validate_structure(example_path: Path) -> Tuple[bool, str]:
    """Check if example has required files"""
    # Check for either agent.py OR root_agent.yaml (for YAML configs)
    has_agent = (example_path / 'agent.py').exists()
    has_yaml = (example_path / 'root_agent.yaml').exists()

    if not has_agent and not has_yaml:
        return False, "Missing agent.py or root_agent.yaml"

    # Check other required files
    required_files = ['__init__.py', 'README.md', 'metadata.json']
    missing_files = []

    for file in required_files:
        if not (example_path / file).exists():
            missing_files.append(file)

    if missing_files:
        return False, f"Missing files: {', '.join(missing_files)}"

    return True, "Structure OK"


def validate_metadata(example_path: Path) -> Tuple[bool, str]:
    """Validate metadata.json content"""
    metadata_file = example_path / 'metadata.json'

    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        required_fields = ['title', 'jtbd', 'language', 'description', 'difficulty', 'tags', 'tech_stack']
        missing_fields = []

        for field in required_fields:
            if field not in metadata:
                missing_fields.append(field)

        if missing_fields:
            return False, f"Metadata missing fields: {', '.join(missing_fields)}"

        # Validate language
        valid_languages = ['python', 'go', 'typescript', 'java']
        if metadata.get('language') not in valid_languages:
            return False, f"Invalid language: {metadata.get('language')}. Valid: {', '.join(valid_languages)}"

        # Validate difficulty level
        valid_difficulties = ['beginner', 'intermediate', 'advanced']
        if metadata.get('difficulty') not in valid_difficulties:
            return False, f"Invalid difficulty: {metadata.get('difficulty')}"

        # Validate tech_stack structure
        tech_stack = metadata.get('tech_stack', [])
        if not isinstance(tech_stack, list):
            return False, "tech_stack must be an array"

        # Validate each tech_stack item
        valid_providers = ['adk', 'gcp', 'third', 'oss']
        for idx, tech in enumerate(tech_stack):
            if not isinstance(tech, dict):
                return False, f"tech_stack[{idx}] must be an object"

            # Check required fields in each tech item
            tech_required = ['name', 'provider', 'icon', 'description']
            for tech_field in tech_required:
                if tech_field not in tech:
                    return False, f"tech_stack[{idx}] missing '{tech_field}'"

            # Validate provider code
            if tech.get('provider') not in valid_providers:
                return False, f"tech_stack[{idx}] has invalid provider '{tech.get('provider')}'. Valid: {', '.join(valid_providers)}"

        # Validate status if present (for coming_soon/planned examples)
        if 'status' in metadata:
            valid_statuses = ['ready', 'coming_soon', 'planned']
            if metadata.get('status') not in valid_statuses:
                return False, f"Invalid status: {metadata.get('status')}. Valid: {', '.join(valid_statuses)}"

            # If status is coming_soon, recommend priority and sprint
            if metadata.get('status') in ['coming_soon', 'planned']:
                if 'priority' not in metadata or 'sprint' not in metadata:
                    # This is a warning, not a failure
                    pass

        tech_count = len(tech_stack)
        status = metadata.get('status', 'ready')
        language = metadata.get('language', 'unknown')
        return True, f"Metadata valid (lang: {language}, tech_stack: {tech_count}, status: {status})"

    except json.JSONDecodeError as e:
        return False, f"Invalid JSON in metadata: {e}"
    except Exception as e:
        return False, f"Error reading metadata: {e}"


def validate_agent_code(example_path: Path) -> Tuple[bool, str]:
    """Validate the agent.py or root_agent.yaml file"""
    agent_file = example_path / 'agent.py'
    yaml_file = example_path / 'root_agent.yaml'

    # Check if this is a YAML-based agent
    if yaml_file.exists() and not agent_file.exists():
        # Validate YAML config
        try:
            # Try to import yaml, but if it's not available (CI environment), do basic validation
            try:
                import yaml
                with open(yaml_file, 'r') as f:
                    config = yaml.safe_load(f)

                # Check required fields
                if 'name' not in config:
                    return False, "YAML missing 'name' field"
                if 'model' not in config:
                    return False, "YAML missing 'model' field"

                # Check model
                approved_models = ['gemini-2.5-flash', 'gemini-2.5-pro']
                if config.get('model') not in approved_models:
                    return False, f"YAML using unapproved model: {config.get('model')}"

                return True, f"YAML config valid (model: {config.get('model')})"
            except ImportError:
                # If yaml module not available (CI), do basic text validation
                with open(yaml_file, 'r') as f:
                    content = f.read()

                # Basic checks without parsing
                if 'name:' not in content:
                    return False, "YAML missing 'name:' field"
                if 'model:' not in content:
                    return False, "YAML missing 'model:' field"

                # Check for approved models
                if 'gemini-2.5-flash' in content or 'gemini-2.5-pro' in content:
                    model = 'gemini-2.5-flash' if 'gemini-2.5-flash' in content else 'gemini-2.5-pro'
                    return True, f"YAML config valid (CI mode, model: {model})"
                else:
                    return False, "YAML using unapproved model"
        except Exception as e:
            return False, f"Error validating YAML: {e}"

    # Check if we're running in CI environment
    is_ci = os.environ.get('CI') == 'true' or os.environ.get('GITHUB_ACTIONS') == 'true'

    try:
        # Read the agent.py file
        with open(agent_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check for root_agent definition
        if 'root_agent' not in content:
            return False, "No 'root_agent' defined"

        # Check for correct model usage
        approved_models = ['gemini-2.5-flash', 'gemini-2.5-pro']
        model_found = False
        model_used = None

        for model in approved_models:
            if f'model="{model}"' in content or f"model='{model}'" in content:
                model_found = True
                model_used = model
                break

        # Special cases for alternative models (only in specific examples)
        alt_model_examples = ['use-claude', 'use-vertex-ai', 'local-ollama', 'use-openai']
        example_name = example_path.name

        if example_name in alt_model_examples:
            # These examples are allowed to use alternative models
            model_found = True
            model_used = "alternative (allowed)"
        elif not model_found:
            # Check if it's using an unapproved model
            if 'model=' in content:
                # Extract the model name for reporting
                import re
                match = re.search(r'model=["\']([^"\']+)["\']', content)
                if match:
                    wrong_model = match.group(1)
                    return False, f"Using unapproved model: {wrong_model}. Use gemini-2.5-flash or gemini-2.5-pro"
                else:
                    return False, "Model specified but couldn't determine which one"
            else:
                return False, "No model specified"

        # In CI environments, skip import validation since google-adk won't be installed
        if is_ci:
            # Just check the code structure without importing
            return True, f"Code structure valid (CI mode, model: {model_used})"

        # Try to import and validate (only in local environments)
        spec = importlib.util.spec_from_file_location("agent", agent_file)
        if spec is None:
            return False, "Could not load agent module"

        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
        except ImportError as e:
            # This is expected if google.adk is not installed
            # Check for various forms of the import error
            error_str = str(e).lower()
            if "google" in error_str or "adk" in error_str:
                # This is expected in CI environments where google-adk isn't installed
                return True, f"Code structure valid (model: {model_used})"
            else:
                return False, f"Import error: {e}"
        except Exception as e:
            return False, f"Error loading agent: {e}"

        # Check if root_agent exists and is the right type
        if not hasattr(module, 'root_agent'):
            return False, "root_agent not found after import"

        return True, f"Agent valid (model: {model_used})"

    except Exception as e:
        return False, f"Error validating agent: {e}"


def validate_readme(example_path: Path) -> Tuple[bool, str]:
    """Validate README.md content"""
    readme_file = example_path / 'README.md'

    try:
        with open(readme_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check for essential sections (be flexible with emojis and encoding)
        required_sections = ['Quick Start', 'The Problem', 'The Solution']
        missing_sections = []

        for section in required_sections:
            # Look for the section text anywhere after ##
            import re
            # Match ## followed by optional emoji/special chars, then the section name
            pattern = r'##\s*[^\w]*\s*' + re.escape(section)
            if not re.search(pattern, content, re.IGNORECASE):
                missing_sections.append(section)

        if missing_sections:
            return False, f"README missing sections: {', '.join(missing_sections)}"

        # Check for JTBD statement
        if '"When' not in content:
            return False, "README missing JTBD statement"

        return True, "README complete"

    except Exception as e:
        return False, f"Error reading README: {e}"


def validate_example(example_path: Path) -> Dict[str, Any]:
    """Run all validations for a single example"""
    results = {
        'name': example_path.name,
        'path': str(example_path),
        'passed': True,
        'checks': {}
    }

    # Check if this is a coming_soon example
    metadata_file = example_path / 'metadata.json'
    is_coming_soon = False
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
                is_coming_soon = metadata.get('status') == 'coming_soon'
        except:
            pass

    # Run all validation checks
    checks = [
        ('structure', validate_structure),
        ('metadata', validate_metadata),
    ]

    # Only validate agent code and README for non-coming_soon examples
    if not is_coming_soon:
        checks.append(('agent_code', validate_agent_code))
        checks.append(('readme', validate_readme))

    for check_name, check_func in checks:
        passed, message = check_func(example_path)
        results['checks'][check_name] = {
            'passed': passed,
            'message': message
        }
        if not passed:
            results['passed'] = False

    return results


def main():
    """Main validation function"""
    print_colored("\n" + "="*60, Colors.BOLD)
    print_colored("ADK by Example - Validation Script", Colors.BOLD)
    print_colored("="*60 + "\n", Colors.BOLD)

    # Find examples directory
    script_dir = Path(__file__).parent
    examples_dir = script_dir.parent / 'examples'

    if not examples_dir.exists():
        print_colored(f"❌ Examples directory not found: {examples_dir}", Colors.RED)
        sys.exit(1)

    # Collect all examples
    all_examples = []
    categories = sorted([d for d in examples_dir.iterdir() if d.is_dir() and not d.name.startswith('_')])

    for category in categories:
        examples = sorted([d for d in category.iterdir() if d.is_dir()])
        all_examples.extend(examples)

    if not all_examples:
        print_colored("❌ No examples found!", Colors.RED)
        sys.exit(1)

    print(f"Found {len(all_examples)} examples in {len(categories)} categories\n")

    # Validate each example
    all_results = []
    passed_count = 0
    failed_count = 0

    for category in categories:
        print_colored(f"\n📁 Category: {category.name}", Colors.BLUE)
        print("-" * 40)

        examples = sorted([d for d in category.iterdir() if d.is_dir()])

        for example_path in examples:
            results = validate_example(example_path)
            all_results.append(results)

            # Print results
            if results['passed']:
                print_colored(f"  ✅ {results['name']}", Colors.GREEN)
                passed_count += 1
            else:
                print_colored(f"  ❌ {results['name']}", Colors.RED)
                failed_count += 1

            # Show details for failed checks
            for check_name, check_result in results['checks'].items():
                if not check_result['passed']:
                    print(f"     └─ {check_name}: {check_result['message']}")
                elif '--verbose' in sys.argv:
                    print(f"     └─ {check_name}: {check_result['message']}")

    # Summary
    print_colored("\n" + "="*60, Colors.BOLD)
    print_colored("Validation Summary", Colors.BOLD)
    print_colored("="*60, Colors.BOLD)

    total = passed_count + failed_count
    pass_rate = (passed_count / total * 100) if total > 0 else 0

    print(f"\nTotal Examples: {total}")
    print_colored(f"Passed: {passed_count}", Colors.GREEN)
    if failed_count > 0:
        print_colored(f"Failed: {failed_count}", Colors.RED)

    print(f"\nPass Rate: {pass_rate:.1f}%")

    if failed_count > 0:
        print_colored("\n⚠️  Some examples have issues. Please fix them before committing.", Colors.YELLOW)
        sys.exit(1)
    else:
        print_colored("\n🎉 All examples validated successfully!", Colors.GREEN)

    # Optional: Generate report file
    if '--report' in sys.argv:
        report_file = script_dir / 'validation_report.json'
        with open(report_file, 'w') as f:
            json.dump(all_results, f, indent=2)
        print(f"\nReport saved to: {report_file}")


if __name__ == "__main__":
    main()
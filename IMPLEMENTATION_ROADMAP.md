# ADK by Example - Implementation Roadmap

## 🎯 Mission
Build a JTBD-focused cookbook that helps developers solve real problems with ADK in < 5 minutes.

## 📋 Phase-by-Phase Implementation Plan

---

## Phase 1: Repository Foundation (Day 1-2)
**Goal**: Establish the core repository structure and configuration

### 1.1 Repository Setup
```bash
# Commands to execute
git init
git remote add origin https://github.com/YOUR_USERNAME/adk-by-example.git
```

### 1.2 Create Core Structure
```
adk-by-example/
├── .gitignore
├── LICENSE (MIT)
├── README.md
├── .env.example
├── examples/
│   └── _shared/
│       ├── __init__.py
│       └── common_tools.py
├── website/
│   └── .gitkeep
├── scripts/
│   └── .gitkeep
├── .github/
│   └── workflows/
│       └── deploy.yml
└── .docs/
    ├── CONTRIBUTING.md
    ├── PROJECT_PLAN.md
    ├── IMPLEMENTATION_ROADMAP.md
    └── GITHUB_PAGES_DEPLOYMENT.md
```

### 1.3 Create .env.example
```bash
# Gemini via Google AI Studio (PRIMARY)
GOOGLE_API_KEY=your-api-key-here

# Gemini via Vertex AI (Alternative)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# For integration examples only
ANTHROPIC_API_KEY=your-anthropic-key
OPENAI_API_KEY=your-openai-key

# OAuth examples
OAUTH_CLIENT_ID=your-oauth-client-id
OAUTH_CLIENT_SECRET=your-oauth-client-secret

# Database examples
FIRESTORE_PROJECT=your-firestore-project
BIGQUERY_DATASET=your-dataset
```

### 1.4 Create .gitignore
```
# Environment
.env
*.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# ADK
.adk/cache/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/
```

### 1.5 Main README.md (Repository Root)
```markdown
# 🚀 ADK by Example

> Copy-paste solutions for common ADK (Agent Development Kit) tasks

## What is this?

ADK by Example provides **working code examples** organized by what you need to accomplish, not by ADK features. Think "I need my agent to search Google" instead of "Chapter 12: Tool Integration".

## Quick Start

1. **Clone & Configure**
   ```bash
   git clone https://github.com/YOUR_USERNAME/adk-by-example.git
   cd adk-by-example
   cp .env.example .env
   # Edit .env with your API keys
   ```

2. **Run Any Example**
   ```bash
   cd examples
   adk web
   # Select any agent from the dropdown
   ```

## 📚 Browse Examples by Need

### 🎯 "I need to get started"
- [`first-agent`](examples/01-getting-started/first-agent) - Working agent in 10 lines
- [`understand-basics`](examples/01-getting-started/understand-basics) - Agent with clear comments
- [`use-config-yaml`](examples/01-getting-started/use-config-yaml) - No-code agent using YAML

### 🔍 "I need to search/fetch data"
- [`search-google`](examples/03-adding-capabilities/search-google) - Web search capability
- [`call-rest-api`](examples/03-adding-capabilities/call-rest-api) - Custom API integration
- [`query-bigquery`](examples/03-adding-capabilities/query-bigquery) - Database access

[... more categories ...]

## Why ADK by Example?

| This Project | Official Docs | Code Samples |
|-------------|---------------|--------------|
| **"I need to..."** problems | Feature reference | Feature demos |
| Copy-paste ready | Conceptual learning | Complex examples |
| 5 min to working code | Deep understanding | Feature exploration |

## Contributing

See [CONTRIBUTING.md](.docs/CONTRIBUTING.md)

## License

MIT - Use these examples freely in your projects!
```

### Deliverables
- [ ] Initialize git repository
- [ ] Create all folders and placeholder files
- [ ] Write .env.example with all variables
- [ ] Create comprehensive .gitignore
- [ ] Write main README.md
- [ ] Create CONTRIBUTING.md

---

## Phase 2: Core Examples (Day 3-5)
**Goal**: Build first 5 working examples from existing ADK samples

### 2.1 Example Priority List (Based on ADK Samples)

| Priority | JTBD Example | Source Sample | Location |
|----------|--------------|---------------|----------|
| 1 | `first-agent` | `hello_world` | `contributing/samples/hello_world/agent.py` |
| 2 | `search-google` | `google_search_agent` | `contributing/samples/google_search_agent/agent.py` |
| 3 | `call-rest-api` | Adapt from `jira_agent` | `contributing/samples/jira_agent/tools.py` |
| 4 | `route-to-experts` | `multi_agent_llm_config` | `contributing/samples/multi_agent_llm_config/` |
| 5 | `chat-with-history` | `history_management` | `contributing/samples/history_management/agent.py` |

### 2.2 Implementation Process for Each Example

1. **Extract from ADK samples**
   - Read source sample from `.adk/adk-python-code-samples.xml`
   - Copy exact code patterns
   - Modify only descriptions and variable names

2. **Create folder structure**
   ```
   examples/[category]/[example-name]/
   ├── __init__.py
   ├── agent.py
   ├── README.md
   ├── metadata.json
   └── test_agent.py (optional)
   ```

3. **Write JTBD-focused README**
   - Clear problem statement
   - Quick start commands
   - Complete working code
   - Sample interactions
   - Troubleshooting

4. **Add metadata.json**
   ```json
   {
     "title": "Search Google for answers",
     "jtbd": "When users ask questions, I need to search the web",
     "difficulty": "beginner",
     "tags": ["tools", "search", "google"],
     "related": ["search-with-grounding", "search-private-data"],
     "source_sample": "google_search_agent"
   }
   ```

5. **Test with adk web**
   ```bash
   cd examples
   adk web
   # Verify agent appears and works
   ```

### Example: first-agent Implementation

```python
# examples/01-getting-started/first-agent/agent.py
"""When I'm new to ADK, I need a working agent in seconds"""
from google.adk import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="first_agent",
    instruction="You are a helpful assistant. Answer questions clearly and concisely."
)
```

```markdown
# examples/01-getting-started/first-agent/README.md
# Create Your First Agent
> "When I'm new to ADK, I need a working agent in seconds"

## 🚀 Quick Start

Run this example:
```bash
cd adk-by-example/examples
adk web
# Select "first_agent" from dropdown
```

## The Problem
You're new to ADK and need to see a working agent immediately to understand the basics.

## The Solution
This minimal agent shows the essential components: importing ADK, creating an agent with a model and instruction.

[... rest of README ...]
```

### Deliverables
- [ ] Implement `first-agent` from hello_world sample
- [ ] Implement `search-google` from google_search_agent sample
- [ ] Implement `call-rest-api` adapted from jira_agent
- [ ] Implement `route-to-experts` from multi_agent_llm_config
- [ ] Implement `chat-with-history` from history_management
- [ ] Test all examples with `adk web`

---

## Phase 3: Category Expansion (Day 6-8)
**Goal**: Build out complete JTBD categories with 2-3 examples each

### 3.1 Categories to Implement

1. **01-getting-started/** (3 examples)
   - ✅ first-agent
   - understand-basics (add detailed comments)
   - use-config-yaml (from yaml_config sample)

2. **02-connecting-llms/** (3 examples)
   - use-gemini-vertex (from vertex samples)
   - use-claude (from hello_world_anthropic)
   - local-ollama (from hello_world_ollama)

3. **03-adding-capabilities/** (4 examples)
   - ✅ search-google
   - ✅ call-rest-api
   - query-bigquery (from bigquery sample)
   - execute-code (from code_execution sample)

4. **04-orchestrating-agents/** (3 examples)
   - ✅ route-to-experts
   - process-pipeline (from simple_sequential_agent)
   - parallel-research (from parallel_functions)

5. **05-managing-context/** (3 examples)
   - ✅ chat-with-history
   - share-between-agents (from session_state_agent)
   - persist-to-firestore (adapt from state examples)

6. **06-going-production/** (3 examples)
   - deploy-cloud-run (from deployment docs)
   - add-monitoring (from telemetry sample)
   - handle-errors (best practices)

### 3.2 Implementation Template
For each new example:
1. Find corresponding sample in `.adk/adk-python-code-samples.xml`
2. Extract and adapt code
3. Write JTBD-focused documentation
4. Create metadata.json
5. Test with `adk web`
6. Add to category README

### Deliverables
- [ ] Complete 01-getting-started (3 examples)
- [ ] Complete 02-connecting-llms (3 examples)
- [ ] Complete 03-adding-capabilities (4 examples)
- [ ] Complete 04-orchestrating-agents (3 examples)
- [ ] Complete 05-managing-context (3 examples)
- [ ] Complete 06-going-production (3 examples)

---

## Phase 4: Automation & Testing (Day 9-10)
**Goal**: Create scripts to validate and maintain examples

### 4.1 Validation Script
```python
# scripts/validate_examples.py
#!/usr/bin/env python3
"""Validate all examples can be loaded by adk web"""

import os
import sys
import json
from pathlib import Path
import subprocess

def validate_example(example_path):
    """Check if example has required files and valid structure"""
    required_files = ['__init__.py', 'agent.py', 'README.md']

    for file in required_files:
        if not (example_path / file).exists():
            return False, f"Missing {file}"

    # Try to import the agent
    try:
        # Add to path and import
        sys.path.insert(0, str(example_path.parent))
        import importlib
        module = importlib.import_module(example_path.name + '.agent')

        # Check for root_agent
        if not hasattr(module, 'root_agent'):
            return False, "No root_agent defined"

        return True, "Valid"
    except Exception as e:
        return False, str(e)

def main():
    examples_dir = Path("examples")

    for category in examples_dir.iterdir():
        if category.is_dir() and not category.name.startswith('_'):
            print(f"\nCategory: {category.name}")

            for example in category.iterdir():
                if example.is_dir():
                    valid, message = validate_example(example)
                    status = "✅" if valid else "❌"
                    print(f"  {status} {example.name}: {message}")

if __name__ == "__main__":
    main()
```

### 4.2 Example Generator Script
```python
# scripts/create_example.py
#!/usr/bin/env python3
"""Scaffold a new JTBD example"""

import os
import json
from pathlib import Path
import argparse

def create_example(category, name, jtbd):
    """Create a new example with standard structure"""

    example_path = Path(f"examples/{category}/{name}")
    example_path.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    (example_path / "__init__.py").touch()

    # Create agent.py template
    agent_code = f'''"""JTBD: {jtbd}"""
from google.adk import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="{name.replace('-', '_')}",
    instruction="TODO: Add instruction"
)
'''

    (example_path / "agent.py").write_text(agent_code)

    # Create README template
    readme = f'''# {name.replace('-', ' ').title()}
> "{jtbd}"

## 🚀 Quick Start

```bash
cd adk-by-example/examples
adk web
# Select "{name}" from dropdown
```

## The Problem
TODO: Describe the specific problem this solves

## The Solution
TODO: Explain the approach

## Complete Code
TODO: Add the full working code

## Try It
TODO: Add sample interactions
'''

    (example_path / "README.md").write_text(readme)

    # Create metadata.json
    metadata = {
        "title": name.replace('-', ' ').title(),
        "jtbd": jtbd,
        "difficulty": "beginner",
        "tags": [],
        "related": []
    }

    (example_path / "metadata.json").write_text(json.dumps(metadata, indent=2))

    print(f"✅ Created example: {example_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("category", help="Category folder (e.g., 01-getting-started)")
    parser.add_argument("name", help="Example name (e.g., first-agent)")
    parser.add_argument("--jtbd", required=True, help="JTBD statement")

    args = parser.parse_args()
    create_example(args.category, args.name, args.jtbd)
```

### Deliverables
- [ ] Create validate_examples.py script
- [ ] Create create_example.py scaffolding script
- [ ] Create test_all.sh script
- [ ] Run validation on all examples
- [ ] Fix any validation errors

---

## Phase 5: Website Development (Day 11-12)
**Goal**: Build simple, searchable static site

### 5.1 Website Structure
```
website/
├── index.html
├── style.css
├── script.js
├── examples.json (generated)
└── CNAME (optional, for custom domain)
```

### 5.2 Generate Examples Index
```python
# scripts/generate_site.py
#!/usr/bin/env python3
"""Generate examples.json for website"""

import json
from pathlib import Path

def generate_examples_json():
    examples = []
    examples_dir = Path("examples")

    for category_dir in examples_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('_'):
            category_name = category_dir.name

            for example_dir in category_dir.iterdir():
                if example_dir.is_dir():
                    metadata_file = example_dir / "metadata.json"

                    if metadata_file.exists():
                        with open(metadata_file) as f:
                            metadata = json.load(f)
                            metadata['category'] = category_name
                            metadata['path'] = f"{category_name}/{example_dir.name}"
                            metadata['id'] = example_dir.name

                            # Read first few lines of README for preview
                            readme_file = example_dir / "README.md"
                            if readme_file.exists():
                                lines = readme_file.read_text().split('\n')
                                # Find the problem section
                                for i, line in enumerate(lines):
                                    if line.startswith("## The Problem"):
                                        if i + 1 < len(lines):
                                            metadata['preview'] = lines[i + 1]
                                        break

                            examples.append(metadata)

    # Sort by category then by title
    examples.sort(key=lambda x: (x['category'], x['title']))

    # Write to website directory
    output_file = Path("website/examples.json")
    output_file.write_text(json.dumps(examples, indent=2))

    print(f"✅ Generated {len(examples)} examples for website")
    return examples

if __name__ == "__main__":
    generate_examples_json()
```

### 5.3 HTML Template (Simplified)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADK by Example - Copy-paste solutions for ADK developers</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>🚀 ADK by Example</h1>
            <p>Copy-paste solutions for common ADK tasks</p>
            <div class="quick-links">
                <a href="https://github.com/YOUR_USERNAME/adk-by-example" class="btn">
                    <svg><!-- GitHub icon --></svg>
                    GitHub
                </a>
                <a href="#getting-started" class="btn primary">Get Started</a>
            </div>
        </div>
    </header>

    <nav>
        <div class="container">
            <input type="search" id="search"
                   placeholder="Search: 'google search', 'deploy', 'oauth'..."
                   autocomplete="off">
            <div id="search-results"></div>
        </div>
    </nav>

    <main class="container">
        <section id="getting-started">
            <h2>🎯 I need to...</h2>
            <div class="categories" id="categories">
                <!-- Generated from examples.json -->
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>Built with ❤️ for the ADK community |
               <a href="https://github.com/YOUR_USERNAME/adk-by-example">Contribute</a>
            </p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

### 5.4 GitHub Actions Deployment
```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Generate site data
        run: |
          python scripts/generate_site.py

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './website'

      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```

### Deliverables
- [ ] Create website HTML structure
- [ ] Write CSS for clean, modern design
- [ ] Implement JavaScript search functionality
- [ ] Create generate_site.py script
- [ ] Set up GitHub Actions workflow
- [ ] Test local preview
- [ ] Deploy to GitHub Pages

---

## Phase 6: Documentation & Polish (Day 13-14)
**Goal**: Complete documentation and prepare for launch

### 6.1 Documentation Tasks
- [ ] Write comprehensive CONTRIBUTING.md
- [ ] Create ARCHITECTURE.md explaining structure
- [ ] Add troubleshooting section to main README
- [ ] Create EXAMPLES_INDEX.md with all examples
- [ ] Write deployment guide

### 6.2 Quality Checklist
- [ ] All examples tested with `adk web`
- [ ] All READMEs follow template
- [ ] All code uses approved models (gemini-2.5-flash/pro)
- [ ] All examples traced to ADK samples
- [ ] No hallucinated code or features
- [ ] Environment variables documented
- [ ] Common errors addressed

### 6.3 Pre-Launch Testing
```bash
# Full test suite
./scripts/test_all.sh

# Checklist:
# 1. Clone fresh copy
git clone [repo-url] test-repo
cd test-repo

# 2. Setup environment
cp .env.example .env
# Add at least GOOGLE_API_KEY

# 3. Test random examples
cd examples
adk web
# Try 5 random agents

# 4. Build website
python scripts/generate_site.py
# Open website/index.html locally

# 5. Verify links
# Check all README links work
# Check GitHub links work
```

---

## Phase 7: Launch (Day 15)
**Goal**: Public release and announcement

### 7.1 Launch Checklist
- [ ] GitHub repo public
- [ ] GitHub Pages enabled
- [ ] All examples working
- [ ] Documentation complete
- [ ] License file added (MIT)
- [ ] Security check (no keys committed)

### 7.2 Launch Materials
1. **GitHub README** - Compelling project description
2. **Website** - Live at github.io
3. **Announcement Post** - For forums/social
4. **Demo Video** - Quick walkthrough (optional)

### 7.3 Announcement Template
```markdown
# Introducing ADK by Example 🚀

Tired of digging through docs to find how to make your agent search Google?

ADK by Example provides copy-paste solutions organized by what you need to do:
- "I need to search the web" → Here's the code
- "I need to call my API" → Here's the code
- "I need to deploy to Cloud Run" → Here's the code

✅ 30+ working examples
✅ All examples work with `adk web`
✅ Single .env configuration
✅ Based on official ADK samples
✅ Free & open source

Check it out: [github.com/YOUR_USERNAME/adk-by-example]
Website: [your-username.github.io/adk-by-example]
```

---

## Success Metrics (Post-Launch)

### Week 1
- [ ] 50+ GitHub stars
- [ ] 10+ forks
- [ ] 100+ website visits
- [ ] 0 critical bugs reported

### Month 1
- [ ] 200+ GitHub stars
- [ ] 50+ forks
- [ ] 5+ community contributions
- [ ] Featured in ADK newsletter/blog

### Ongoing
- [ ] Monthly updates with new examples
- [ ] Sync with ADK releases
- [ ] Community feedback integration
- [ ] Example request tracking

---

## Timeline Summary

| Phase | Days | Key Deliverables |
|-------|------|------------------|
| 1. Foundation | 1-2 | Repository structure, .env, README |
| 2. Core Examples | 3-5 | 5 working examples from ADK samples |
| 3. Category Expansion | 6-8 | 20+ examples across all categories |
| 4. Automation | 9-10 | Validation scripts, generators |
| 5. Website | 11-12 | Static site with search |
| 6. Documentation | 13-14 | Complete docs, testing |
| 7. Launch | 15 | Public release |

**Total: 15 days from start to launch** 🚀

---

## Next Immediate Actions

1. **Today**: Create repository and basic structure
2. **Tomorrow**: Implement first 3 examples
3. **This Week**: Complete Phase 1-2
4. **Next Week**: Complete Phase 3-5
5. **Week 3**: Polish and launch

---

## Notes

- Prioritize examples that solve real problems developers face
- Every example must be grounded in existing ADK samples
- Use only `gemini-2.5-flash` and `gemini-2.5-pro` models
- Test everything with `adk web` before committing
- Keep examples simple and focused on one problem
- Link related examples to create learning paths
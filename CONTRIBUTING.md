# Contributing to ADK by Example

Thank you for your interest in contributing to ADK by Example! This guide will help you add your own example to share with the community.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Creating Your Example](#creating-your-example)
4. [File Structure](#file-structure)
5. [Metadata Requirements](#metadata-requirements)
6. [Writing Your Agent Code](#writing-your-agent-code)
7. [Writing Documentation](#writing-documentation)
8. [Testing Locally](#testing-locally)
9. [Running Validation](#running-validation)
10. [Submitting Your Pull Request](#submitting-your-pull-request)
11. [Must-Haves Checklist](#must-haves-checklist)
12. [Best Practices](#best-practices)
13. [Getting Help](#getting-help)

---

## Prerequisites

Before you start, make sure you have:

- **Git** installed on your machine
- **Python 3.11+** installed
- **Google ADK** installed (`pip install google-adk`)
- A **GitHub account**
- **~30 minutes** of your time
- An **API key** (Google AI Studio or Vertex AI)

---

## Setting Up Your Environment

### 1. Fork and Clone

First, fork the repository on GitHub, then clone it:

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/adk-by-example.git
cd adk-by-example
```

### 2. Set Up Environment Variables

```bash
# Copy the environment template
cp .env.example .env

# Edit .env and add your API keys
# For Google AI Studio (free tier):
GOOGLE_API_KEY=your_api_key_here

# Or for Vertex AI:
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
```

### 3. Install Dependencies

```bash
pip install google-adk
```

### 4. Create a New Branch

```bash
git checkout -b add-your-example-name
```

---

## Creating Your Example

We provide a scaffold script to create the example structure for you:

```bash
python scripts/create_example.py \
  --category "03-adding-capabilities" \
  --name "your-feature-name" \
  --jtbd "When users need X, I need to accomplish Y" \
  --status "ready" \
  --priority "medium" \
  --sprint 1
```

**Category options:**
- `01-getting-started` - First steps with ADK
- `02-connecting-llms` - Integrating different LLMs
- `03-adding-capabilities` - Tools and functionality
- `04-orchestrating-agents` - Multi-agent systems
- `05-managing-context` - State and memory
- `06-going-production` - Deployment and monitoring
- `07-advanced-patterns` - Complex patterns

This creates:
```
examples/XX-category/your-example/
├── __init__.py
├── agent.py
├── metadata.json
└── README.md
```

---

## File Structure

Every example **must** have these files:

```
your-example/
├── __init__.py           # Empty file (required for Python package)
├── agent.py             # Your agent code (must export root_agent)
├── metadata.json        # Metadata for the website
└── README.md            # Documentation following our template
```

Optional files:
```
├── requirements.txt     # If you need special dependencies
└── root_agent.yaml      # Alternative to agent.py (YAML config only)
```

---

## Metadata Requirements

Your `metadata.json` must include all required fields:

```json
{
  "title": "Clear, descriptive title",
  "jtbd": "When [situation], I need to [task], so I can [outcome]",
  "language": "python",
  "tech_stack": [
    {
      "name": "Technology Name",
      "provider": "adk",
      "icon": "🤖",
      "description": "Brief description of what this does"
    }
  ],
  "description": "One sentence describing what this example does",
  "difficulty": "beginner",
  "tags": ["tag1", "tag2", "tag3"],
  "related": ["other-example-1", "other-example-2"],
  "source_sample": "official_adk_sample_name",
  "time_to_complete": "5 minutes"
}
```

**Field explanations:**

- **title**: Clear, user-facing title (e.g., "Search Google for Answers")
- **jtbd**: Jobs-to-be-Done format explaining the use case
- **language**: Must be one of: `python`, `go`, `typescript`, `java`
- **tech_stack**: Array of technologies used (see Tech Stack section below)
- **description**: One sentence summary
- **difficulty**: `beginner`, `intermediate`, or `advanced`
- **tags**: Relevant keywords for search
- **related**: Slugs of related examples
- **source_sample**: Name of the official ADK sample this is based on
- **time_to_complete**: How long to complete (e.g., "5 minutes")

### Tech Stack Providers

Use these provider codes:

- **`adk`** - ADK components (Agent, FunctionTool, etc.)
- **`gcp`** - Google Cloud Platform services (Gemini, Vertex AI, BigQuery)
- **`third`** - Third-party services (Claude, OpenAI, A2A Protocol)
- **`oss`** - Open source libraries (Pydantic, FastAPI, LangChain)

Example tech_stack:
```json
"tech_stack": [
  {
    "name": "Gemini",
    "provider": "gcp",
    "icon": "🔮",
    "description": "Google's LLM via AI Studio"
  },
  {
    "name": "LLM Agent",
    "provider": "adk",
    "icon": "🤖",
    "description": "ADK's intelligent agent"
  }
]
```

---

## Writing Your Agent Code

### Critical Rules

Your `agent.py` **must** follow these rules:

✅ **DO:**
- Use `gemini-2.5-flash` or `gemini-2.5-pro` as the default model
- Base your code on official ADK samples (in `.adk/adk-python-code-samples.xml`)
- Export a variable named `root_agent`
- Include a docstring with the JTBD statement
- Add helpful comments explaining key parts

❌ **DON'T:**
- Invent code patterns - always reference official samples
- Use unapproved models (unless it's a model integration example)
- Include API keys or secrets in the code
- Create overly complex examples

### Template Structure

```python
"""When [situation], I need to [task], so I can [outcome]"""

from google.adk import Agent
# Add other imports as needed

# Main agent (MUST be named root_agent)
root_agent = Agent(
    model="gemini-2.5-flash",
    name="your_agent_name",
    instruction="Clear, specific instructions for the agent's behavior"
)
```

### Example with Tools

```python
"""When users ask questions, I need to search the web for answers"""

from google.adk import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="""You are a helpful assistant that searches the web.
    When users ask questions, use the google_search tool to find current information.
    Provide comprehensive answers with sources.""",
    tools=[google_search]
)
```

### Finding Source Samples

All your code should be based on official ADK samples. Find them in:
- `.adk/adk-python-code-samples.xml` - Full working examples
- `.adk/adk-docs-documentation.xml` - API documentation

Common source samples:
- `hello_world` - Basic agent
- `google_search_agent` - Google Search integration
- `jira_agent` - REST API calls with tools
- `multi_agent_llm_config` - Multi-agent coordination
- `code_execution` - Code execution capability
- `history_management` - Chat history

---

## Writing Documentation

Your `README.md` must follow this template:

```markdown
# [Clear Problem Statement]
> "When I [situation], I need to [task], so I can [outcome]"

## 🚀 Quick Start

\`\`\`bash
cd examples
adk web
# Select "your-example-name" from dropdown
# Ask: "sample question to test with"
\`\`\`

## 📋 The Problem

[1-2 sentences describing the specific scenario this solves]

## ✅ The Solution

[Brief explanation of how this example solves the problem]

## 💻 Complete Code

\`\`\`python
# Your full agent.py code with inline comments
\`\`\`

## 🧪 Try It

1. Set your API key in `.env` (see root `.env.example`)
2. Run `adk web` from the examples directory
3. Select "your-example-name" from the dropdown
4. Ask: "sample question"

Expected response: [what the agent should do]

## 📚 What You'll Learn

- How to [concept 1]
- How to [concept 2]
- How to [concept 3]

## 🔧 Customize

- To add [feature X], modify line Y in agent.py
- To change [behavior Z], update the instruction parameter

## ➡️ Next Steps

- **Simpler**: Try `[basic-example]` for [reason]
- **More complex**: Try `[advanced-example]` for [reason]
- **Different approach**: See `[alternative-example]` using [technique]
```

---

## Testing Locally

Before submitting, test your example thoroughly:

### 1. Test with ADK Web

```bash
cd examples
adk web
```

- Select your example from the dropdown
- Test with various queries
- Verify it works as expected
- Check for errors in the console

### 2. Verify File Permissions

```bash
# Make sure all files are readable
ls -la examples/XX-category/your-example/
```

---

## Running Validation

**This is mandatory before submitting your PR.**

### 1. Validate Your Example

```bash
python scripts/validate_examples.py
```

**Expected output:**
```
✅ your-example
   └─ structure: Structure OK
   └─ metadata: Metadata valid (lang: python, tech_stack: 2, status: ready)
   └─ agent_code: Agent valid (model: gemini-2.5-flash)
   └─ readme: README complete

Passed: 36
Pass Rate: 100.0%

🎉 All examples validated successfully!
```

If you see errors, fix them before proceeding.

### 2. Regenerate Website Data

```bash
python scripts/generate_site.py
```

**Expected output:**
```
✅ Generated examples.json with 36 examples
   Categories: Getting Started, Connecting to LLMs, ...
   Languages: python (36)
   Output: /Users/.../website/examples.json
```

---

## Submitting Your Pull Request

### 1. Stage Your Changes

```bash
# Add your example files
git add examples/XX-category/your-example/

# Add regenerated website data
git add website/examples.json

# Check what you're committing
git status
```

### 2. Commit Your Changes

**Important:** Follow our commit message format (no AI attribution):

```bash
git commit -m "Add your-example-name example

- Solves [specific problem]
- Based on [official_adk_sample]
- Uses [key technologies]
- Tested and validated"
```

✅ **Good commit messages:**
```
Add google-search example
Add multi-agent routing pattern
Add code execution capability
```

❌ **Bad commit messages:**
```
Add example by Claude
Update files
New feature
```

### 3. Push to Your Fork

```bash
git push origin add-your-example-name
```

### 4. Create Pull Request

1. Go to https://github.com/lavinigam-gcp/adk-by-example
2. Click "Pull Requests" → "New Pull Request"
3. Click "compare across forks"
4. Select your fork and branch
5. Fill out the PR template (auto-populated)
6. Click "Create Pull Request"

### 5. PR Review Process

After submitting:

1. **Automated checks** run (validation must pass ✅)
2. **Core team reviews** your example
3. **Feedback** provided if changes needed
4. **Approval** once everything looks good
5. **Merge** to main branch
6. **Live** on website within minutes! 🎉

---

## Must-Haves Checklist

Before submitting, verify all items:

### Content Quality
- [ ] Example solves a real, specific problem
- [ ] JTBD statement is clear and user-focused
- [ ] Code is based on official ADK samples
- [ ] README follows the template structure
- [ ] Instructions are clear and complete

### Technical Requirements
- [ ] Uses `gemini-2.5-flash` or `gemini-2.5-pro` (unless model integration example)
- [ ] All required files present (`__init__.py`, `agent.py`, `metadata.json`, `README.md`)
- [ ] `language` field in metadata.json
- [ ] `tech_stack` array properly formatted
- [ ] Agent exports `root_agent` variable

### Testing
- [ ] Tested with `adk web` and works correctly
- [ ] Validation script passes 100%
- [ ] No API keys or secrets in code
- [ ] Example works out of the box with `.env` setup

### Documentation
- [ ] README includes all required sections
- [ ] Sample queries provided
- [ ] Related examples linked
- [ ] Clear customization instructions

### Git
- [ ] Branch name descriptive (e.g., `add-google-search`)
- [ ] Commit message clear and concise
- [ ] No AI attribution in commits
- [ ] Only relevant files committed

---

## Best Practices

### Writing Great Examples

✅ **DO:**
- Keep it simple (KISS principle)
- One example = one clear use case
- Add helpful inline comments
- Link to related examples
- Test thoroughly before submitting
- Use descriptive variable names
- Follow Python PEP 8 style guide

❌ **DON'T:**
- Create overly complex examples
- Mix multiple unrelated features
- Use obscure or undocumented APIs
- Skip validation checks
- Include unnecessary dependencies
- Hard-code values that should be configurable

### JTBD Best Practices

Good JTBD statements:
- ✅ "When I need to analyze customer feedback, I need to categorize sentiment"
- ✅ "When debugging production issues, I need to query application logs"
- ✅ "When building chatbots, I need to maintain conversation history"

Poor JTBD statements:
- ❌ "Use the sentiment analysis API"
- ❌ "Query logs"
- ❌ "Chat history"

### Documentation Best Practices

- Start with the problem, not the solution
- Provide concrete examples users can copy-paste
- Explain the "why" behind key decisions
- Include expected outputs
- Link to official documentation for deep dives

---

## Getting Help

Need assistance? We're here to help!

### Resources

- **Documentation**: [https://lavinigam-gcp.github.io/adk-by-example/](https://lavinigam-gcp.github.io/adk-by-example/)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/lavinigam-gcp/adk-by-example/discussions)
- **Issues**: [Report bugs or request features](https://github.com/lavinigam-gcp/adk-by-example/issues)
- **Official ADK Docs**: [https://github.com/google/adk](https://github.com/google/adk)

### Common Issues

**Validation fails:**
- Check error message carefully
- Ensure all required files exist
- Verify JSON syntax in metadata.json
- Make sure `language` field is present

**Example not showing in `adk web`:**
- Ensure `__init__.py` exists
- Check that `agent.py` exports `root_agent`
- Run from `examples/` directory
- Restart `adk web` after changes

**PR checks failing:**
- Run `python scripts/validate_examples.py` locally
- Fix any validation errors
- Push fixes to your branch
- Checks will re-run automatically

---

## Code of Conduct

By contributing, you agree to:

- Be respectful and professional
- Provide constructive feedback
- Help others in the community
- Follow contribution guidelines
- Respect core team decisions

We're building this together! 🚀

---

## Thank You!

Your contributions help the entire ADK community. We appreciate your time and effort! ❤️

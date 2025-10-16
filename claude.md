# ADK by Example - Implementation Guide

## ⚠️ CRITICAL REQUIREMENTS

### Model Usage (MANDATORY)
1. **PRIMARY MODELS**: Always use `gemini-2.5-flash` or `gemini-2.5-pro`
2. **ALTERNATIVE MODELS**: Only for specific integration examples (see below)
3. **GROUNDING**: ALL code MUST come from `.adk/adk-docs-documentation.xml` or `.adk/adk-python-code-samples.xml`

### Approved Model Names (from ADK samples)
```python
# PRIMARY (use these by default)
model="gemini-2.5-flash"  # Standard examples
model="gemini-2.5-pro"    # Complex examples

# ALTERNATIVES (only for integration demos)
# Claude via native ADK
from google.adk.models.anthropic_llm import Claude
model=Claude(model="claude-3-5-sonnet-v2@20241022")

# Via LiteLLM
from google.adk.models.lite_llm import LiteLlm
model=LiteLlm(model="openai/gpt-4o")  # OpenAI
model=LiteLlm(model="vertex_ai/claude-3-7-sonnet")  # Vertex Claude
model=LiteLlm(model="ollama_chat/mistral-small3.1")  # Ollama
```

## Project Vision
**ADK by Example** - A Jobs-to-be-Done focused cookbook for ADK developers. Think "Go by Example" but organized by what developers need to accomplish, not by features.

## Core Innovation
While official docs explain "what is an LLM Agent", we answer "I need my agent to search Google and summarize results - show me the code!"

## Folder Structure (Optimized for `adk web`)

```
adk-by-example/
├── .env.example         # ← Users copy this ONCE to .env
├── examples/           # ← Run `adk web` from here
│   ├── [All agent examples organized by JTBD]
```

### Key Design Decisions:

1. **Single .env Setup**: User sets API keys once at root, all examples inherit
2. **Flat Agent Structure**: Each example is a valid agent folder for `adk web`
3. **Reusable Samples**: Leverage existing ADK samples but reformat for JTBD
4. **Copy-Paste Ready**: Every example works immediately after cloning

## Example Structure

Each example MUST have:
```
example-name/
├── __init__.py         # Required for Python package
├── agent.py           # Main agent (or root_agent.yaml for config)
├── README.md          # JTBD-focused documentation
└── metadata.json      # For website generation
```

## JTBD Categories (Problem-First)

### 1. "I need to get started quickly"
- `first-agent` - Minimal working agent in 10 lines
- `understand-basics` - Agent with clear comments explaining each part
- `use-config-yaml` - No-code agent using YAML

### 2. "I need to connect to an AI model"
- `use-gemini-free` - Quick start with free API key
- `use-vertex-ai` - Production setup with GCP
- `use-local-ollama` - Offline development

### 3. "I need my agent to search/fetch data"
- `search-google` - Web search capability
- `call-rest-api` - Custom API integration
- `query-bigquery` - Database access

### 4. "I need multiple agents working together"
- `route-to-experts` - Coordinator pattern
- `review-improve` - Critic-refiner loop
- `parallel-research` - Concurrent execution

### 5. "I need to deploy to production"
- `deploy-cloud-run` - Serverless deployment
- `add-monitoring` - Observability setup
- `handle-auth` - OAuth integration

## First 5 Examples to Build

### 1. first-agent
```python
# agent.py
"""When I'm new to ADK, I need a working agent in seconds"""
from google.adk import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="first_agent",
    instruction="You are a helpful assistant. Answer questions clearly and concisely."
)
```

### 2. search-google
```python
# agent.py
"""When users ask questions, I need to search the web for answers"""
from google.adk import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="Search for information and provide comprehensive answers with sources.",
    tools=[google_search]
)
```

### 3. call-my-api
```python
# agent.py
"""When integrating with my system, I need to call my REST API"""
from google.adk import Agent
import requests

def get_user_data(user_id: str) -> dict:
    """Fetch user data from our API"""
    # In production, use environment variables for base URL
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

root_agent = Agent(
    model="gemini-2.5-flash",
    name="api_agent",
    instruction="Help users by fetching their data when needed.",
    tools=[get_user_data]
)
```

### 4. route-to-experts
```python
# agent.py
"""When handling diverse requests, I need to delegate to specialists"""
from google.adk import Agent

billing_agent = Agent(
    name="billing_expert",
    model="gemini-2.5-flash",
    instruction="You handle billing inquiries. Explain charges, payment methods, and billing cycles.",
    description="Handles billing and payment questions"
)

technical_agent = Agent(
    name="technical_expert",
    model="gemini-2.5-flash",
    instruction="You handle technical issues. Troubleshoot problems and explain technical concepts.",
    description="Handles technical support questions"
)

root_agent = Agent(
    name="coordinator",
    model="gemini-2.5-flash",
    instruction="""Route customer inquiries to the right expert:
    - Billing questions → billing_expert
    - Technical issues → technical_expert
    Always be polite and ensure the customer gets helped.""",
    sub_agents=[billing_agent, technical_agent]
)
```

### 5. deploy-cloud-run
```python
# agent.py
"""When going to production, I need to deploy to Cloud Run"""
from google.adk import Agent
import os

root_agent = Agent(
    model="gemini-2.5-flash",
    name="production_agent",
    instruction="Production-ready agent with environment configuration.",
    # Production configurations
    generate_content_config={
        "temperature": 0.7,
        "max_output_tokens": 1000
    }
)

# Dockerfile (in same folder)
"""
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["adk", "api_server", "--port", "8080"]
"""

# deploy.sh
"""
gcloud run deploy my-agent \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
"""
```

## README Template for Each Example

```markdown
# [Clear Problem Statement]
> "When [situation], I need to [task], so I can [outcome]"

## 🚀 Quick Start

```bash
# Option 1: Use this example directly
cd adk-by-example/examples
adk web
# Select "[example-name]" from dropdown

# Option 2: Copy to your project
cp -r [example-name] ~/my-project/
cd ~/my-project
adk web
```

## 📋 The Problem
[1-2 sentences about the specific scenario]

## ✅ The Solution
[How this example solves it]

## 💻 Complete Code
[Full working code with comments]

## 🧪 Try It
1. Set your API key in `.env` (see root .env.example)
2. Run `adk web`
3. Ask: "[sample question]"

## 📚 What You'll Learn
- How to [concept 1]
- How to [concept 2]
- How to [concept 3]

## 🔧 Customize
- To add [feature X], modify line Y
- To change [behavior Z], update...

## ➡️ Next Steps
- **More complex**: Try `[advanced-example]` for [reason]
- **Different approach**: See `[alternative]` using [technique]
- **Production ready**: Check `[deployment-example]`
```

## Website Structure (Simple GitHub Pages)

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>ADK by Example</title>
    <style>
        /* Minimal, clean styling */
    </style>
</head>
<body>
    <header>
        <h1>ADK by Example</h1>
        <p>Copy-paste solutions for common ADK tasks</p>
    </header>

    <nav>
        <input type="search" placeholder="Search: 'call API', 'deploy', 'OAuth'...">
    </nav>

    <main>
        <section class="jtbd-category">
            <h2>I need to get started</h2>
            <div class="examples">
                <a href="#first-agent">
                    <h3>Create my first agent</h3>
                    <p>Working agent in 10 lines</p>
                    <code>adk create my-agent --from first-agent</code>
                </a>
            </div>
        </section>
    </main>
</body>
</html>
```

## CRITICAL: Implementation Guidelines

### Code Sourcing Rules
1. **NEVER INVENT CODE** - Every example MUST be based on actual samples from:
   - `.adk/adk-python-code-samples.xml` (40+ working samples)
   - `.adk/adk-docs-documentation.xml` (official documentation)

2. **Verification Process** - Before creating any example:
   - Search for similar functionality in existing samples
   - Copy the exact pattern/structure
   - Modify only the minimum necessary (variable names, descriptions)
   - Preserve all imports, configurations, and patterns

3. **Model Selection Priority**:
   - Default: `model="gemini-2.5-flash"`
   - Complex: `model="gemini-2.5-pro"`
   - Integration demos only: Use exact model names from samples

### Example Mapping (Source → JTBD)
| JTBD Example | Source Sample | Location in .adk files |
|--------------|---------------|------------------------|
| `first-agent` | `hello_world` | `contributing/samples/hello_world/agent.py` |
| `search-google` | `google_search_agent` | `contributing/samples/google_search_agent/agent.py` |
| `call-my-api` | Adapt from `jira_agent` tools | `contributing/samples/jira_agent/tools.py` |
| `route-to-experts` | `multi_agent_llm_config` | `contributing/samples/multi_agent_llm_config/` |
| `deploy-cloud-run` | Deploy section in docs | `.adk/adk-docs-documentation.xml` |
| `use-claude` | `hello_world_anthropic` | `contributing/samples/hello_world_anthropic/agent.py` |
| `local-ollama` | `hello_world_ollama` | `contributing/samples/hello_world_ollama/agent.py` |
| `oauth-integration` | `oauth_calendar_agent` | `contributing/samples/oauth_calendar_agent/agent.py` |
| `execute-code` | `code_execution` | `contributing/samples/code_execution/agent.py` |
| `stream-responses` | `live_bidi_streaming_single_agent` | `contributing/samples/live_bidi_streaming_single_agent/` |

## Implementation Roadmap

### Week 1: Foundation
- [x] Create project structure
- [x] Write PROJECT_PLAN.md
- [ ] Set up repository
- [ ] Create .env.example with all variables
- [ ] Build first 5 examples (using exact code from samples)

### Week 2: Core Examples
- [ ] Port 10 high-value examples from existing samples
- [ ] Standardize README format
- [ ] Create validation script
- [ ] Test with `adk web`

### Week 3: Expansion
- [ ] Add 10 more examples
- [ ] Create website
- [ ] Add search functionality
- [ ] Write contribution guide

### Week 4: Polish & Launch
- [ ] Test all examples
- [ ] Generate website
- [ ] Create launch post
- [ ] Publish to GitHub

## Key Differentiators

1. **Problem-First Navigation**: Find examples by what you need to do, not by ADK features
2. **Zero to Running in 60 Seconds**: Clone → adk web → working agent
3. **Real-World Focus**: Examples solve actual developer problems, not toy demos
4. **Progressive Learning**: Each example links to simpler/more complex variations
5. **Production-Ready Patterns**: Include deployment, monitoring, error handling

## Validation Checklist

Each example MUST:
- [ ] Have a clear JTBD in the title
- [ ] Work with `adk web` without modification
- [ ] Include complete, runnable code
- [ ] Provide sample queries/interactions
- [ ] Link to related examples
- [ ] Reference official docs for deep-dives
- [ ] Include common troubleshooting

## Success Metrics

- **Adoption**: 100+ GitHub stars in first month
- **Usability**: <5 minutes from discovery to working agent
- **Coverage**: 80% of common use cases covered
- **Quality**: 0 broken examples per release

## Notes for Implementation

1. **Leverage Existing Samples**: Most content exists in `/contributing/samples/`. We're reformatting for JTBD, not recreating.

2. **Environment Variables**: Single `.env` at root means users configure once. All examples use `os.getenv()`.

3. **Folder Naming**: Use verbs and outcomes: `search-google`, `deploy-cloud-run`, `handle-errors`

4. **Metadata for Website**: Each example has `metadata.json`:
```json
{
  "title": "Search Google for answers",
  "jtbd": "When users ask questions, I need to search the web",
  "difficulty": "beginner",
  "tags": ["tools", "search", "google"],
  "related": ["search-with-grounding", "search-private-data"]
}
```

5. **Testing**: Script that runs `adk web` for each example and validates it starts

## Next Actions

1. Create GitHub repository
2. Set up basic folder structure
3. Create .env.example
4. Implement first 3 examples
5. Test with `adk web`
6. Get feedback from team
7. Iterate and expand
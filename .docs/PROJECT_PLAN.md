# ADK by Example - Project Plan

## Executive Summary

**ADK by Example** is a Jobs-to-be-Done (JTBD) focused resource that helps developers quickly solve real-world challenges when building with the Agent Development Kit. Unlike traditional documentation that explains features, this project provides copy-paste-ready solutions organized by developer needs.

## ⚠️ CRITICAL: Model Usage Requirements

### PRIMARY MODELS (Use these by default)
- **`gemini-2.5-flash`** - For all standard examples
- **`gemini-2.5-pro`** - For complex/advanced examples requiring more capability

### ALTERNATIVE MODELS (Only when demonstrating specific integrations)
Based on actual ADK samples in `.adk/adk-python-code-samples.xml`:

#### Via Native ADK Integration:
```python
# Anthropic Claude (from hello_world_anthropic sample)
from google.adk.models.anthropic_llm import Claude
model = Claude(model="claude-3-5-sonnet-v2@20241022")
```

#### Via LiteLLM Integration:
```python
from google.adk.models.lite_llm import LiteLlm

# OpenAI (from hello_world_litellm sample)
model = LiteLlm(model="openai/gpt-4o")

# Vertex AI Claude (from telemetry sample)
model = LiteLlm(model="vertex_ai/claude-3-7-sonnet")

# Ollama local models (from hello_world_ollama sample)
model = LiteLlm(model="ollama_chat/mistral-small3.1")
```

### GROUNDING RULE
**ALL examples, model names, configurations, and code MUST be directly sourced from:**
- `.adk/adk-docs-documentation.xml` (ADK documentation)
- `.adk/adk-python-code-samples.xml` (ADK Python samples)

**NEVER use model names or configurations not found in these files.**

## Core Principles

### 1. JTBD-First Approach
- **Format**: "When I [situation], I need to [task], so I can [outcome]"
- **Problem-driven**: Start with the developer's problem, not ADK's features
- **Complete solutions**: Each example is a fully working agent, not a snippet
- **Progressive complexity**: Link simpler → complex examples

### 2. Optimized for `adk web`
- All examples work with `adk web` command out-of-the-box
- Standardized folder structure for consistency
- Shared `.env` configuration at root level
- Clear replication instructions using `adk create`

### 3. Non-Overlapping with Docs
- **Official Docs**: How ADK works (reference)
- **Code Samples**: Feature demonstrations (learning)
- **ADK by Example**: Solving specific problems (doing)

## Project Structure

```
adk-by-example/
├── .env.example                    # Global environment template
├── .env                           # User's actual env (gitignored)
├── README.md                      # Project homepage
├── examples/                      # All JTBD examples
│   ├── _shared/                  # Shared utilities
│   │   ├── __init__.py
│   │   └── common_tools.py
│   │
│   ├── 01-getting-started/       # Starting journey
│   │   ├── first-agent/
│   │   │   ├── __init__.py
│   │   │   ├── agent.py
│   │   │   ├── README.md
│   │   │   └── requirements.txt
│   │   ├── chat-with-history/
│   │   ├── api-key-setup/
│   │   └── ...
│   │
│   ├── 02-connecting-llms/       # Model integration
│   │   ├── switch-to-gemini/
│   │   ├── use-claude/
│   │   ├── local-ollama/
│   │   └── ...
│   │
│   ├── 03-adding-capabilities/   # Tool integration
│   │   ├── search-google/
│   │   ├── call-my-api/
│   │   ├── query-database/
│   │   └── ...
│   │
│   ├── 04-orchestrating-agents/  # Multi-agent patterns
│   │   ├── delegate-to-experts/
│   │   ├── process-pipeline/
│   │   ├── parallel-research/
│   │   └── ...
│   │
│   ├── 05-managing-context/      # State & memory
│   │   ├── remember-conversation/
│   │   ├── share-between-agents/
│   │   ├── persist-to-firestore/
│   │   └── ...
│   │
│   ├── 06-going-production/      # Deployment
│   │   ├── deploy-cloud-run/
│   │   ├── add-monitoring/
│   │   ├── handle-errors/
│   │   └── ...
│   │
│   └── 07-advanced-patterns/     # Complex scenarios
│       ├── stream-responses/
│       ├── human-approval/
│       ├── custom-workflow/
│       └── ...
│
├── website/                       # Simple showcase site
│   ├── index.html
│   ├── style.css
│   └── examples.json             # Generated from examples/
│
└── scripts/                       # Automation
    ├── validate_examples.py       # Test all examples
    ├── generate_site.py          # Build website
    └── create_example.py         # Scaffold new example
```

## Example Template

Each example follows this structure:

### Folder Structure
```
example-name/
├── __init__.py           # Required for Python package
├── agent.py             # Main agent code (or root_agent.yaml)
├── README.md            # Documentation
├── requirements.txt     # Python dependencies (if special)
├── tools.py            # Custom tools (optional)
└── test_agent.py       # Basic test (optional)
```

### README Template
```markdown
# [Clear Problem Statement]
> "When I need to [specific task], so I can [outcome]"

## Quick Start

```bash
# Copy this example
adk create my-[example-name] --from-example [example-name]

# Or manually:
cp -r examples/[category]/[example-name] ~/my-agents/
cd ~/my-agents
adk web
```

## The Problem
[1-2 sentences explaining the specific scenario]

## The Solution
[Brief explanation of the approach]

## Code
[Main code with comments - must be complete and runnable]

## How to Run
1. Set environment variables (see root .env.example)
2. Run `adk web` from parent directory
3. Select agent and test with: "[sample query]"

## What You'll Learn
- ✓ [Key concept 1]
- ✓ [Key concept 2]
- ✓ [Key concept 3]

## Common Issues
- **Issue**: [Common problem]
  **Solution**: [How to fix]

## Next Steps
- Try: [Related example 1] - [Why it's relevant]
- Try: [Related example 2] - [Different approach]
- Docs: [Link to detailed docs]
```

## Environment Management

### Global `.env.example`
```bash
# Gemini via Google AI Studio
GOOGLE_API_KEY=your-api-key-here

# Gemini via Vertex AI
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Claude (Anthropic)
ANTHROPIC_API_KEY=your-anthropic-key

# OpenAI
OPENAI_API_KEY=your-openai-key

# OAuth (for authenticated tools)
OAUTH_CLIENT_ID=your-oauth-client-id
OAUTH_CLIENT_SECRET=your-oauth-client-secret

# Database connections
FIRESTORE_PROJECT=your-firestore-project
BIGQUERY_DATASET=your-dataset
```

Users copy `.env.example` to `.env` once, and all examples use these variables.

## JTBD Categories (Refined)

### 1. Starting My First Agent
**Job**: "I need to create and run an agent quickly"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `first-agent` | "When I'm new to ADK, I need to create my first working agent" | `hello_world` |
| `chat-with-history` | "When building a chatbot, I need to maintain conversation context" | `history_management` |
| `api-key-setup` | "When starting development, I need to configure my API keys properly" | - |
| `test-locally` | "When developing, I need to test my agent quickly without deployment" | - |

### 2. Connecting to LLMs
**Job**: "I need to use a specific AI model"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `switch-to-gemini` | "When migrating from OpenAI, I need to use Gemini instead" | - |
| `use-claude` | "When I prefer Anthropic, I need to integrate Claude" | `hello_world_anthropic` |
| `local-ollama` | "When offline or testing, I need to run models locally" | `hello_world_ollama` |
| `compare-models` | "When optimizing, I need to compare responses from different models" | - |

### 3. Adding Capabilities
**Job**: "I need my agent to do something specific"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `search-google` | "When users ask questions, I need to search the web" | `google_search_agent` |
| `call-my-api` | "When integrating with my system, I need to call my REST API" | - |
| `query-database` | "When accessing data, I need to query BigQuery/Spanner" | `bigquery`, `spanner` |
| `execute-code` | "When processing data, I need to run Python code safely" | `code_execution` |
| `oauth-integration` | "When accessing user data, I need OAuth authentication" | `oauth_calendar_agent` |

### 4. Orchestrating Multiple Agents
**Job**: "I need agents to work together"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `delegate-to-experts` | "When handling diverse requests, I need to route to specialist agents" | `multi_agent_llm_config` |
| `process-pipeline` | "When processing data, I need agents to work in sequence" | `simple_sequential_agent` |
| `parallel-research` | "When researching, I need agents to work simultaneously" | `parallel_functions` |
| `review-loop` | "When quality matters, I need agents to review and improve output" | `multi_agent_loop_config` |

### 5. Managing State & Context
**Job**: "I need to remember and share information"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `remember-conversation` | "When chatting, I need to remember previous messages" | `memory` |
| `share-between-agents` | "When coordinating, I need agents to share data" | `session_state_agent` |
| `persist-to-firestore` | "When scaling, I need to store state in a database" | - |
| `use-memory-bank` | "When building memory, I need Vertex AI Memory Bank" | - |

### 6. Going to Production
**Job**: "I need to deploy and monitor my agent"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `deploy-cloud-run` | "When going live, I need to deploy to Cloud Run" | - |
| `add-monitoring` | "When in production, I need to track performance" | `telemetry` |
| `handle-errors` | "When things fail, I need graceful error handling" | - |
| `rate-limiting` | "When scaling, I need to control request rates" | - |

### 7. Advanced Patterns
**Job**: "I need to implement complex behaviors"

| Example | JTBD | Existing Sample |
|---------|------|-----------------|
| `stream-responses` | "When improving UX, I need real-time streaming" | `live_bidi_streaming_single_agent` |
| `human-approval` | "When risk is high, I need human confirmation" | `human_in_loop` |
| `custom-workflow` | "When logic is complex, I need custom orchestration" | - |
| `a2a-integration` | "When distributed, I need agents to communicate remotely" | `a2a_basic` |

## Implementation Requirements

### Grounding to ADK Sources (MANDATORY)
Every example MUST be directly derived from:

1. **Primary Source**: `.adk/adk-python-code-samples.xml`
   - Contains 40+ working samples
   - Each sample has been tested and verified
   - Use exact code patterns, imports, and configurations

2. **Documentation Source**: `.adk/adk-docs-documentation.xml`
   - Official ADK documentation
   - Configuration guidelines
   - Deployment instructions

### Example Source Mapping
Each JTBD example maps to specific existing samples:

| JTBD Category | Example | Source Sample | File Path |
|---------------|---------|---------------|-----------|
| Getting Started | `first-agent` | `hello_world` | `contributing/samples/hello_world/` |
| Getting Started | `chat-with-history` | `history_management` | `contributing/samples/history_management/` |
| Tools | `search-google` | `google_search_agent` | `contributing/samples/google_search_agent/` |
| Tools | `query-database` | `bigquery`, `spanner` | `contributing/samples/bigquery/`, `spanner/` |
| Tools | `oauth-integration` | `oauth_calendar_agent` | `contributing/samples/oauth_calendar_agent/` |
| Multi-Agent | `delegate-to-experts` | `multi_agent_llm_config` | `contributing/samples/multi_agent_llm_config/` |
| Multi-Agent | `process-pipeline` | `simple_sequential_agent` | `contributing/samples/simple_sequential_agent/` |
| Multi-Agent | `parallel-research` | `parallel_functions` | `contributing/samples/parallel_functions/` |
| State | `remember-conversation` | `memory` | `contributing/samples/memory/` |
| State | `share-between-agents` | `session_state_agent` | `contributing/samples/session_state_agent/` |
| Advanced | `stream-responses` | `live_bidi_streaming_single_agent` | `contributing/samples/live_bidi_streaming_single_agent/` |
| Advanced | `human-approval` | `human_in_loop` | `contributing/samples/human_in_loop/` |
| Advanced | `a2a-integration` | `a2a_basic` | `contributing/samples/a2a_basic/` |

## Implementation Phases

### Phase 1: Foundation (Week 1-2)
1. Set up repository structure
2. Create example template and guidelines
3. Build 5 core examples (using EXACT code from samples):
   - `first-agent` (from `hello_world`)
   - `search-google` (from `google_search_agent`)
   - `call-my-api` (adapt from `jira_agent` tools)
   - `delegate-to-experts` (from `multi_agent_llm_config`)
   - `deploy-cloud-run` (from deployment docs)

### Phase 2: Core Examples (Week 3-4)
1. Port 10 more high-value examples from existing samples
2. Ensure consistent structure and documentation
3. Create validation script
4. Build simple website

### Phase 3: Expansion (Week 5-6)
1. Add remaining examples
2. Create `create_example.py` script
3. Add integration tests
4. Polish website with search/filter

### Phase 4: Launch (Week 7)
1. Final testing of all examples
2. Documentation review
3. Create launch materials
4. Publish to GitHub

## Success Metrics

1. **Time to First Success**: < 5 minutes from clone to running agent
2. **Example Coverage**: 30+ examples covering 80% of common use cases
3. **Copy-Paste Success Rate**: 100% of examples work without modification
4. **Developer Satisfaction**: Measure via GitHub stars and feedback

## Differentiation from Existing Resources

| Resource | Focus | Format | Use Case |
|----------|-------|--------|----------|
| **Official Docs** | How ADK works | Reference guides | Learning concepts |
| **Code Samples** | Feature demos | Complex examples | Understanding features |
| **ADK by Example** | Solving problems | Copy-paste solutions | Getting things done |
| **Tutorials** | Step-by-step learning | Long-form guides | Deep understanding |

## Website Features

### Simple Static Site
- **Home**: Problem-focused navigation
- **Browse by Job**: JTBD categories
- **Search**: Find by keywords, error messages
- **Copy Button**: One-click code copying
- **Run Instructions**: Clear setup for each example

### Example Page
- Problem statement
- Complete code (syntax highlighted)
- Copy button
- "Open in GitHub" link
- "Create locally" command
- Related examples

## Maintenance

### Per-Release Tasks
1. Test all examples with new ADK version
2. Update deprecated patterns
3. Add examples for new features
4. Update website

### Contribution Guidelines
1. Examples must solve a specific problem
2. Code must be complete and runnable
3. Follow the template structure
4. Include test file
5. Update website index

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Examples break with ADK updates | Automated testing on releases |
| Overlap with official docs | Clear differentiation in README |
| Too many examples to maintain | Focus on high-value JTBD only |
| Complex setup requirements | Shared .env, clear instructions |

## Next Steps

1. Create repository with basic structure
2. Initialize with 3 example categories
3. Port 5 existing samples to new format
4. Build minimal website
5. Get feedback from ADK team
6. Iterate and expand
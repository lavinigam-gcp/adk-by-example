#!/usr/bin/env python3
"""
Populate tech_stack fields for all coming_soon examples based on ADK documentation.
"""
import json
from pathlib import Path

# Tech stack definitions based on ADK documentation
TECH_STACKS = {
    # 02-connecting-llms
    "use-gemini-free": [
        {"name": "Google AI Studio", "provider": "gcp", "icon": "🎨", "description": "Free tier API access for Gemini models"},
        {"name": "Gemini API", "provider": "gcp", "icon": "✨", "description": "Direct API access via GOOGLE_API_KEY"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agent powered by Gemini"}
    ],
    "use-vertex-ai": [
        {"name": "Vertex AI", "provider": "gcp", "icon": "🔷", "description": "Enterprise-grade Gemini deployment platform"},
        {"name": "Service Account", "provider": "gcp", "icon": "🔑", "description": "GCP authentication for production"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agent with Vertex AI backend"}
    ],
    "use-claude": [
        {"name": "Claude API", "provider": "third", "icon": "🤖", "description": "Anthropic's Claude model API"},
        {"name": "LiteLLM", "provider": "oss", "icon": "🔀", "description": "Unified LLM interface library"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agent with Claude backend"}
    ],
    "local-ollama": [
        {"name": "Ollama", "provider": "oss", "icon": "🦙", "description": "Local LLM runtime for offline development"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agent with local Ollama backend"}
    ],
    "compare-models": [
        {"name": "LiteLLM", "provider": "oss", "icon": "🔀", "description": "Unified interface to 100+ LLM providers"},
        {"name": "Multiple LLMs", "provider": "third", "icon": "🎯", "description": "Compare Gemini, Claude, GPT side-by-side"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agents for evaluation tasks"}
    ],

    # 03-adding-capabilities (remaining 4)
    "query-bigquery": [
        {"name": "BigQuery", "provider": "gcp", "icon": "📊", "description": "Google Cloud data warehouse"},
        {"name": "FunctionTool", "provider": "adk", "icon": "🔧", "description": "Wrap BigQuery queries as tools"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent that queries data on demand"}
    ],
    "execute-code": [
        {"name": "Code Execution", "provider": "adk", "icon": "⚙️", "description": "Safe Python code execution sandbox"},
        {"name": "FunctionTool", "provider": "adk", "icon": "🔧", "description": "Wrap code execution as a tool"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent that generates and runs code"}
    ],
    "search-documents": [
        {"name": "Vertex AI Search", "provider": "gcp", "icon": "🔍", "description": "Enterprise document search and grounding"},
        {"name": "Grounding", "provider": "adk", "icon": "📎", "description": "Ground LLM responses in your documents"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent with enterprise RAG capabilities"}
    ],

    # 04-orchestrating-agents (already done - keeping for reference)
    "custom-orchestration": [
        {"name": "Custom Agent", "provider": "adk", "icon": "🎛️", "description": "Build custom orchestration logic"},
        {"name": "BaseAgent", "provider": "adk", "icon": "🏗️", "description": "Extend BaseAgent for unique workflows"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Sub-agents in custom orchestration"}
    ],

    # 05-managing-context
    "chat-with-history": [
        {"name": "Session State", "provider": "adk", "icon": "💾", "description": "Maintain conversation history"},
        {"name": "InvocationContext", "provider": "adk", "icon": "📋", "description": "Pass context across turns"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent with memory of past interactions"}
    ],
    "share-between-agents": [
        {"name": "Session State", "provider": "adk", "icon": "💾", "description": "Shared state dictionary for agents"},
        {"name": "output_key", "provider": "adk", "icon": "🔑", "description": "Store agent results in state"},
        {"name": "Multi-Agent", "provider": "adk", "icon": "🤝", "description": "Agents sharing data via state"}
    ],
    "persist-to-firestore": [
        {"name": "Firestore", "provider": "gcp", "icon": "🔥", "description": "NoSQL database for state persistence"},
        {"name": "Session State", "provider": "adk", "icon": "💾", "description": "Persist agent state to database"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent with durable memory"}
    ],
    "manage-artifacts": [
        {"name": "GCS Artifacts", "provider": "gcp", "icon": "📦", "description": "Google Cloud Storage for files"},
        {"name": "Artifact Service", "provider": "adk", "icon": "📁", "description": "Manage files and artifacts"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent that works with files"}
    ],
    "long-term-memory": [
        {"name": "Memory Bank", "provider": "gcp", "icon": "🧠", "description": "Vertex AI long-term memory storage"},
        {"name": "Session State", "provider": "adk", "icon": "💾", "description": "Bridge to Memory Bank"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🤖", "description": "Agent with persistent memory"}
    ],

    # 06-going-production (remaining 3)
    "use-remote-a2a": [
        {"name": "RemoteA2aAgent", "provider": "adk", "icon": "🔌", "description": "Consume remote A2A agents as tools"},
        {"name": "A2A Protocol", "provider": "third", "icon": "🌐", "description": "Agent-to-Agent communication standard"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Main agent using remote agents"}
    ],
    "add-monitoring": [
        {"name": "OpenTelemetry", "provider": "oss", "icon": "📡", "description": "Observability and tracing framework"},
        {"name": "Cloud Trace", "provider": "gcp", "icon": "📊", "description": "GCP distributed tracing"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Instrumented agent with telemetry"}
    ],
    "handle-errors": [
        {"name": "Callbacks", "provider": "adk", "icon": "🔔", "description": "Event handlers for errors"},
        {"name": "Try/Catch", "provider": "adk", "icon": "🛡️", "description": "Error handling patterns"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Resilient agent with error handling"}
    ],

    # 07-advanced-patterns
    "stream-responses": [
        {"name": "Streaming", "provider": "adk", "icon": "📡", "description": "Real-time bidirectional streaming"},
        {"name": "WebSocket", "provider": "oss", "icon": "🔌", "description": "Live connection for streaming"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent with streaming responses"}
    ],
    "human-approval": [
        {"name": "Human-in-Loop", "provider": "adk", "icon": "👤", "description": "Manual approval workflow pattern"},
        {"name": "get_user_choice", "provider": "adk", "icon": "✋", "description": "Built-in tool for user confirmation"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent that requests approval"}
    ],
    "use-mcp-servers": [
        {"name": "MCP Protocol", "provider": "third", "icon": "🔌", "description": "Model Context Protocol standard"},
        {"name": "MCPToolset", "provider": "adk", "icon": "🧰", "description": "Integrate MCP servers and tools"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "Agent using MCP tools"}
    ],
    "integrate-langchain": [
        {"name": "LangChain", "provider": "oss", "icon": "⛓️", "description": "Popular LLM framework"},
        {"name": "LangchainTool", "provider": "adk", "icon": "🔧", "description": "Wrapper for LangChain tools"},
        {"name": "LLM Agent", "provider": "adk", "icon": "🧠", "description": "ADK agent using LangChain tools"}
    ],
}


def update_metadata(example_name: str, tech_stack: list):
    """Update metadata.json with tech_stack"""
    examples_dir = Path(__file__).parent.parent / "examples"

    # Find the metadata.json file for this example
    metadata_files = list(examples_dir.glob(f"*/{example_name}/metadata.json"))

    if not metadata_files:
        print(f"❌ Could not find metadata for {example_name}")
        return False

    metadata_file = metadata_files[0]

    with open(metadata_file, 'r') as f:
        metadata = json.load(f)

    # Update tech_stack
    metadata['tech_stack'] = tech_stack

    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ Updated {example_name}")
    return True


def main():
    print("🚀 Populating tech_stack fields based on ADK documentation...\n")

    updated = 0
    failed = 0

    for example_name, tech_stack in TECH_STACKS.items():
        if update_metadata(example_name, tech_stack):
            updated += 1
        else:
            failed += 1

    print(f"\n📊 Summary:")
    print(f"   ✅ Updated: {updated}")
    print(f"   ❌ Failed: {failed}")
    print(f"\nNext: Run 'python scripts/generate_site.py' to regenerate the website")


if __name__ == "__main__":
    main()

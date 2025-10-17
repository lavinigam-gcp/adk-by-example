#!/bin/bash
# Create all 23 placeholder examples for ADK by Example

set -e  # Exit on error

echo "🚀 Creating 23 placeholder examples..."
echo ""

# Category 02: Connecting to LLMs (5 examples)
echo "📁 Category 02: Connecting to LLMs (5 examples)"
python scripts/create_example.py \
  --category "02-connecting-llms" \
  --name "use-gemini-free" \
  --jtbd "When I want to start fast with free API, I need Google AI Studio" \
  --description "Quick start with Gemini using free Google AI Studio API key" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "beginner" \
  --time "3 minutes" \
  --source "hello_world with AI Studio" \
  --tags "llm" "gemini" "ai-studio" "free"

python scripts/create_example.py \
  --category "02-connecting-llms" \
  --name "use-vertex-ai" \
  --jtbd "When I need production Gemini, I need Vertex AI integration" \
  --description "Production-ready Gemini deployment with Vertex AI and service accounts" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "vertex_ai_agent" \
  --tags "llm" "gemini" "vertex-ai" "production"

python scripts/create_example.py \
  --category "02-connecting-llms" \
  --name "use-claude" \
  --jtbd "When I prefer Anthropic models, I need Claude integration" \
  --description "Integrate Anthropic's Claude models via direct API or LiteLLM" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "7 minutes" \
  --source "hello_world_anthropic" \
  --tags "llm" "claude" "anthropic" "litellm"

python scripts/create_example.py \
  --category "02-connecting-llms" \
  --name "local-ollama" \
  --jtbd "When I want offline development, I need local models" \
  --description "Run LLMs locally with Ollama for offline development and testing" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "beginner" \
  --time "8 minutes" \
  --source "hello_world_ollama" \
  --tags "llm" "ollama" "local" "offline"

python scripts/create_example.py \
  --category "02-connecting-llms" \
  --name "compare-models" \
  --jtbd "When I need to choose the right model, I need comparison framework" \
  --description "Compare multiple LLM providers using LiteLLM for best model selection" \
  --status "coming_soon" \
  --priority "low" \
  --sprint 4 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "LiteLLM documentation" \
  --tags "llm" "litellm" "comparison" "evaluation"

echo "✅ Created 5 examples in 02-connecting-llms"
echo ""

# Category 03: Adding Capabilities (4 more examples, search-google already exists)
echo "📁 Category 03: Adding Capabilities (4 new examples)"
python scripts/create_example.py \
  --category "03-adding-capabilities" \
  --name "call-rest-api" \
  --jtbd "When I need to integrate APIs, I need REST API calling capability" \
  --description "Integrate with any REST API using FunctionTool for data access" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "jira_agent" \
  --tags "api" "rest" "function-tool" "integration"

python scripts/create_example.py \
  --category "03-adding-capabilities" \
  --name "query-bigquery" \
  --jtbd "When I need database access, I need to query BigQuery" \
  --description "Query BigQuery databases for data-driven agent responses" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "bigquery sample" \
  --tags "database" "bigquery" "sql" "gcp"

python scripts/create_example.py \
  --category "03-adding-capabilities" \
  --name "execute-code" \
  --jtbd "When I need computation, I need safe code execution" \
  --description "Execute Python code safely for calculations and data processing" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "code_execution sample" \
  --tags "code-execution" "computation" "sandbox"

python scripts/create_example.py \
  --category "03-adding-capabilities" \
  --name "search-documents" \
  --jtbd "When I need enterprise RAG, I need document search capability" \
  --description "Add Vertex AI Search for enterprise document grounding and RAG" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "vertex_ai_search sample" \
  --tags "rag" "search" "vertex-ai" "grounding"

echo "✅ Created 4 examples in 03-adding-capabilities"
echo ""

# Category 04: Orchestrating Agents (5 examples - CRITICAL for PM feedback)
echo "📁 Category 04: Orchestrating Agents (5 examples)"
python scripts/create_example.py \
  --category "04-orchestrating-agents" \
  --name "route-to-experts" \
  --jtbd "When I need multiple agents collaborating, I need specialist routing" \
  --description "Build a multi-agent system with coordinator routing to specialist agents" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "multi_agent_llm_config" \
  --tags "multi-agent" "orchestration" "agent-tool" "delegation"

python scripts/create_example.py \
  --category "04-orchestrating-agents" \
  --name "process-pipeline" \
  --jtbd "When my workflow is always the same, I need sequential processing" \
  --description "Create deterministic pipelines with Sequential Agent for step-by-step workflows" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "simple_sequential_agent" \
  --tags "sequential" "workflow" "pipeline"

python scripts/create_example.py \
  --category "04-orchestrating-agents" \
  --name "parallel-research" \
  --jtbd "When I need concurrent execution, I need parallel agents" \
  --description "Execute multiple agents in parallel for concurrent research and data gathering" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "parallel_functions" \
  --tags "parallel" "concurrent" "fan-out"

python scripts/create_example.py \
  --category "04-orchestrating-agents" \
  --name "iterative-refinement" \
  --jtbd "When I want a critique agent reviewing output, I need loop patterns" \
  --description "Use Loop Agent for iterative refinement with critic-reviewer pattern" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "loop_agent sample" \
  --tags "loop" "iterative" "refinement" "critique"

python scripts/create_example.py \
  --category "04-orchestrating-agents" \
  --name "custom-orchestration" \
  --jtbd "When I need dynamic planning, I need custom orchestration logic" \
  --description "Build custom orchestration with dynamic task planning and routing" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "advanced" \
  --time "20 minutes" \
  --source "custom_agent sample" \
  --tags "custom" "planning" "orchestration" "dynamic"

echo "✅ Created 5 examples in 04-orchestrating-agents"
echo ""

# Category 05: Managing Context (5 examples)
echo "📁 Category 05: Managing Context (5 examples)"
python scripts/create_example.py \
  --category "05-managing-context" \
  --name "chat-with-history" \
  --jtbd "When I need conversation memory, I need session state management" \
  --description "Maintain conversation history and context across multiple turns" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "beginner" \
  --time "8 minutes" \
  --source "history_management" \
  --tags "session-state" "memory" "conversation" "history"

python scripts/create_example.py \
  --category "05-managing-context" \
  --name "share-between-agents" \
  --jtbd "When agents need to pass data, I need shared session state" \
  --description "Share data between agents using shared session state" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "session_state_agent" \
  --tags "session-state" "shared-state" "multi-agent"

python scripts/create_example.py \
  --category "05-managing-context" \
  --name "persist-to-firestore" \
  --jtbd "When I need durable storage, I need Firestore persistence" \
  --description "Store agent state persistently in Firestore for durability" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "firestore_state sample" \
  --tags "firestore" "persistence" "storage" "gcp"

python scripts/create_example.py \
  --category "05-managing-context" \
  --name "manage-artifacts" \
  --jtbd "When I need to store files, I need artifact management" \
  --description "Store and retrieve files using GCS Artifacts and Artifact Service" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "gcs_artifacts sample" \
  --tags "artifacts" "files" "gcs" "storage"

python scripts/create_example.py \
  --category "05-managing-context" \
  --name "long-term-memory" \
  --jtbd "When I need memory across sessions, I need Memory Bank" \
  --description "Use Vertex AI Memory Bank for long-term agent memory" \
  --status "coming_soon" \
  --priority "low" \
  --sprint 4 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "memory_bank sample" \
  --tags "memory-bank" "vertex-ai" "long-term" "memory"

echo "✅ Created 5 examples in 05-managing-context"
echo ""

# Category 06: Going to Production (5 examples - CRITICAL for "expose to world")
echo "📁 Category 06: Going to Production (5 examples)"
python scripts/create_example.py \
  --category "06-going-production" \
  --name "deploy-cloud-run" \
  --jtbd "When I need serverless deployment, I need Cloud Run integration" \
  --description "Deploy your agent to Cloud Run for serverless production hosting" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "15 minutes" \
  --source "cloud_run deployment docs" \
  --tags "cloud-run" "deployment" "production" "gcp"

python scripts/create_example.py \
  --category "06-going-production" \
  --name "expose-via-a2a" \
  --jtbd "When my agents need to be exposed to world, I need A2A protocol" \
  --description "Expose your agent as an A2A microservice for world accessibility" \
  --status "coming_soon" \
  --priority "critical" \
  --sprint 1 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "a2a_basic" \
  --tags "a2a" "protocol" "microservices" "api"

python scripts/create_example.py \
  --category "06-going-production" \
  --name "use-remote-a2a" \
  --jtbd "When I need to call remote agents, I need A2A client" \
  --description "Consume remote A2A agents as tools in your agent" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "a2a_consuming sample" \
  --tags "a2a" "remote" "client" "distributed"

python scripts/create_example.py \
  --category "06-going-production" \
  --name "add-monitoring" \
  --jtbd "When I need observability, I need monitoring and telemetry" \
  --description "Add OpenTelemetry monitoring for production observability" \
  --status "coming_soon" \
  --priority "high" \
  --sprint 2 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "telemetry sample" \
  --tags "monitoring" "opentelemetry" "observability" "production"

python scripts/create_example.py \
  --category "06-going-production" \
  --name "handle-errors" \
  --jtbd "When things fail, I need robust error handling" \
  --description "Implement robust error handling patterns with try/catch and callbacks" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "10 minutes" \
  --source "error_handling best practices" \
  --tags "error-handling" "callbacks" "resilience"

echo "✅ Created 5 examples in 06-going-production"
echo ""

# Category 07: Advanced Patterns (4 examples)
echo "📁 Category 07: Advanced Patterns (4 examples)"
python scripts/create_example.py \
  --category "07-advanced-patterns" \
  --name "stream-responses" \
  --jtbd "When I need real-time updates, I need streaming responses" \
  --description "Implement bidirectional streaming for real-time agent responses" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "live_bidi_streaming_single_agent" \
  --tags "streaming" "realtime" "websocket"

python scripts/create_example.py \
  --category "07-advanced-patterns" \
  --name "human-approval" \
  --jtbd "When I need manual approval, I need human-in-the-loop pattern" \
  --description "Add human approval steps to agent workflows for safety" \
  --status "coming_soon" \
  --priority "medium" \
  --sprint 3 \
  --difficulty "intermediate" \
  --time "12 minutes" \
  --source "human_in_loop" \
  --tags "human-in-loop" "approval" "confirmation"

python scripts/create_example.py \
  --category "07-advanced-patterns" \
  --name "use-mcp-servers" \
  --jtbd "When I want to use MCP tools, I need MCP integration" \
  --description "Integrate Model Context Protocol (MCP) servers and tools" \
  --status "coming_soon" \
  --priority "low" \
  --sprint 4 \
  --difficulty "advanced" \
  --time "15 minutes" \
  --source "mcp_integration sample" \
  --tags "mcp" "protocol" "tools"

python scripts/create_example.py \
  --category "07-advanced-patterns" \
  --name "integrate-langchain" \
  --jtbd "When I want LangChain tools, I need LangChain integration" \
  --description "Use LangChain tools within ADK agents via LangchainTool wrapper" \
  --status "coming_soon" \
  --priority "low" \
  --sprint 4 \
  --difficulty "advanced" \
  --time "12 minutes" \
  --source "langchain_tool sample" \
  --tags "langchain" "integration" "tools"

echo "✅ Created 4 examples in 07-advanced-patterns"
echo ""

echo "🎉 Successfully created all 23 placeholder examples!"
echo ""
echo "Next steps:"
echo "  1. Regenerate website: python scripts/generate_site.py"
echo "  2. Validate examples: python scripts/validate_examples.py"
echo "  3. Manually add tech_stack to each metadata.json"

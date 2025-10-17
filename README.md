# 🚀 ADK by Example

> **Copy-paste solutions for common ADK (Agent Development Kit) tasks**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Examples](https://img.shields.io/badge/examples-7-green)](./examples)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini-4285F4)](https://ai.google.dev/)
[![Website](https://img.shields.io/badge/website-live-brightgreen)](https://lavinigam-gcp.github.io/adk-by-example/)

## What is ADK by Example?

ADK by Example provides **working code examples** organized by what you need to accomplish, not by ADK features.

Instead of reading through documentation to understand concepts, find exactly what you need:
- 🔍 **"I need my agent to search Google"** → Here's the code
- 🔗 **"I need to call my REST API"** → Copy this example
- 🚢 **"I need to deploy to Cloud Run"** → Follow these steps
- 🤝 **"I need multiple agents working together"** → Use this pattern

Think of it as **Stack Overflow's best answers**, but organized and tested.

## 🌐 Browse Examples Online

Visit **[https://lavinigam-gcp.github.io/adk-by-example/](https://lavinigam-gcp.github.io/adk-by-example/)** to:

- 🔍 **Search by what you need**: "I want to search Google", "deploy my agent"
- 🌙 **Dark mode support**: Automatically detects your system preference
- 📱 **Mobile-friendly**: Responsive design works on all devices
- ⚡ **Quick actions**: One-click copy for all commands
- ♿ **Accessible**: WCAG 2.1 AA compliant with keyboard navigation
- 🏷️ **Smart filtering**: Filter by category and search simultaneously

## 🎯 Quick Start

### 1. Clone & Configure (30 seconds)

```bash
# Clone the repository
git clone https://github.com/lavinigam-gcp/adk-by-example.git
cd adk-by-example

# Set up your environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY (minimum requirement)
```

### 2. Run Any Example (30 seconds)

```bash
# Navigate to examples directory
cd examples

# Start ADK web interface
adk web

# Select any agent from the dropdown and start chatting!
```

### 3. Copy to Your Project

```bash
# Option 1: Copy specific example
cp -r examples/01-getting-started/first-agent ~/my-project/

# Option 2: Use as reference and build your own
cat examples/03-adding-capabilities/search-google/agent.py
```

## 📚 Browse Examples by What You Need

### 🎯 "I need to get started"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`first-agent`](examples/01-getting-started/first-agent) | Working agent in 10 lines of code | ⭐ |
| [`understand-basics`](examples/01-getting-started/understand-basics) | Agent with detailed comments explaining each part | ⭐ |
| [`use-config-yaml`](examples/01-getting-started/use-config-yaml) | No-code agent using YAML configuration | ⭐ |

### 🤖 "I need to connect to an AI model"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`use-gemini-free`](examples/02-connecting-llms/use-gemini-free) | Quick start with free Google AI Studio key | ⭐ |
| [`use-vertex-ai`](examples/02-connecting-llms/use-vertex-ai) | Production setup with Google Cloud | ⭐⭐ |
| [`use-claude`](examples/02-connecting-llms/use-claude) | Integrate Anthropic's Claude | ⭐⭐ |
| [`local-ollama`](examples/02-connecting-llms/local-ollama) | Run models locally for offline development | ⭐⭐ |

### 🔍 "I need my agent to search/fetch data"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`search-google`](examples/03-adding-capabilities/search-google) | Add web search capability to your agent | ⭐ |
| [`call-rest-api`](examples/03-adding-capabilities/call-rest-api) | Integrate with any REST API | ⭐⭐ |
| [`query-bigquery`](examples/03-adding-capabilities/query-bigquery) | Query BigQuery databases | ⭐⭐ |
| [`execute-code`](examples/03-adding-capabilities/execute-code) | Run Python code safely | ⭐⭐⭐ |

### 👥 "I need multiple agents working together"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`route-to-experts`](examples/04-orchestrating-agents/route-to-experts) | Coordinator routing to specialist agents | ⭐⭐ |
| [`process-pipeline`](examples/04-orchestrating-agents/process-pipeline) | Sequential processing pipeline | ⭐⭐ |
| [`parallel-research`](examples/04-orchestrating-agents/parallel-research) | Concurrent agent execution | ⭐⭐⭐ |
| [`review-loop`](examples/04-orchestrating-agents/review-loop) | Critic-refiner pattern | ⭐⭐⭐ |

### 💾 "I need to manage state and context"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`chat-with-history`](examples/05-managing-context/chat-with-history) | Maintain conversation history | ⭐ |
| [`share-between-agents`](examples/05-managing-context/share-between-agents) | Share data between agents | ⭐⭐ |
| [`persist-to-firestore`](examples/05-managing-context/persist-to-firestore) | Store state in database | ⭐⭐ |

### 🚀 "I need to deploy to production"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`deploy-cloud-run`](examples/06-going-production/deploy-cloud-run) | Deploy to Cloud Run | ⭐⭐ |
| [`add-monitoring`](examples/06-going-production/add-monitoring) | Add telemetry and monitoring | ⭐⭐ |
| [`handle-errors`](examples/06-going-production/handle-errors) | Robust error handling | ⭐⭐ |
| [`rate-limiting`](examples/06-going-production/rate-limiting) | Implement rate limits | ⭐⭐⭐ |

### 🎨 "I need advanced patterns"
| Example | Description | Difficulty |
|---------|-------------|------------|
| [`stream-responses`](examples/07-advanced-patterns/stream-responses) | Real-time streaming output | ⭐⭐⭐ |
| [`human-approval`](examples/07-advanced-patterns/human-approval) | Human-in-the-loop pattern | ⭐⭐⭐ |
| [`custom-workflow`](examples/07-advanced-patterns/custom-workflow) | Complex orchestration logic | ⭐⭐⭐ |

## 🛠️ Environment Setup

### Minimal Setup (Just to get started)
```bash
# You only need one API key to start
GOOGLE_API_KEY=your-key-here  # Get free at https://aistudio.google.com/app/apikey
```

### Full Setup (For all examples)
See [`.env.example`](.env.example) for all available configuration options.

## 📂 Repository Structure

```
adk-by-example/
├── examples/                    # All runnable examples
│   ├── 01-getting-started/     # Beginner examples
│   ├── 02-connecting-llms/     # Model integrations
│   ├── 03-adding-capabilities/ # Tools and APIs
│   ├── 04-orchestrating-agents/# Multi-agent patterns
│   ├── 05-managing-context/    # State management
│   ├── 06-going-production/    # Deployment
│   └── 07-advanced-patterns/   # Complex scenarios
├── website/                     # Documentation site
├── scripts/                     # Utility scripts
│   ├── validate_examples.py    # Test all examples
│   └── create_example.py       # Scaffold new example
├── .env.example                # Environment template
└── README.md                   # You are here
```

## 🤝 How This Differs From Official Resources

| Resource | Focus | Best For | Format |
|----------|-------|----------|--------|
| **ADK by Example** | Solving specific problems | "I need to..." scenarios | Copy-paste code |
| **Official Docs** | Understanding ADK concepts | Learning how ADK works | Reference guide |
| **Code Samples** | Demonstrating features | Exploring capabilities | Complex demos |
| **Tutorials** | Step-by-step learning | Deep understanding | Long-form guides |

## 🎯 Design Principles

1. **JTBD-First**: Organized by what developers need to do, not by features
2. **Copy-Paste Ready**: Every example works immediately after cloning
3. **Minimal Setup**: Single `.env` file configuration for all examples
4. **Real-World Focus**: Examples solve actual problems, not toy demos
5. **Progressive Learning**: Start simple, link to more complex variations
6. **Well-Tested**: All examples verified with `adk web` command
7. **Grounded in Reality**: Every example based on official ADK samples

## 🚦 Getting Help

### Quick Troubleshooting

**Problem**: "Agent not showing in adk web"
- **Solution**: Ensure `__init__.py` exists in the example folder

**Problem**: "Import errors when running"
- **Solution**: Run from the `examples/` directory, not from individual example folders

**Problem**: "API key errors"
- **Solution**: Check `.env` file exists and contains valid `GOOGLE_API_KEY`

### Resources

- 📖 [Official ADK Documentation](https://github.com/google/adk)
- 💬 [GitHub Issues](https://github.com/lavinigam-gcp/adk-by-example/issues)
- 🌟 [Contributing Guide](.docs/CONTRIBUTING.md)

## 📈 Roadmap

- [x] **Phase 1**: Repository structure and foundation (✅ Complete)
- [x] **Phase 2**: Getting Started category with 6 examples (✅ Complete)
- [x] **Phase 3**: Production-ready website with advanced search (✅ Complete)
  - [x] JTBD-focused search with smart query processing
  - [x] Dark mode with system preference detection
  - [x] Full accessibility (WCAG 2.1 AA)
  - [x] Mobile-responsive design
  - [x] Category filtering and URL persistence
- [ ] **Phase 4**: 30+ JTBD examples across all 7 categories (23% complete - 7/30)
- [ ] **Phase 5**: Community contributions and integrations
- [ ] **Phase 6**: Video tutorials for complex patterns

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](.docs/CONTRIBUTING.md) for guidelines.

Quick contribution ideas:
- 🐛 Report issues with examples
- 📝 Improve documentation
- 🎯 Suggest new JTBD scenarios
- 🔧 Submit your own examples

## 📜 License

MIT License - see [LICENSE](LICENSE) file. Use these examples freely in your projects!

## 🙏 Acknowledgments

- Built on top of [Google's ADK](https://github.com/google/adk)
- Inspired by [Go by Example](https://gobyexample.com)
- Powered by [Gemini](https://ai.google.dev/)

---

<p align="center">
  Made with ❤️ for the ADK community
  <br>
  <a href="https://github.com/lavinigam-gcp/adk-by-example">⭐ Star this repo</a> if you find it helpful!
  <br>
  <a href="https://lavinigam-gcp.github.io/adk-by-example/">🌐 Browse examples online</a>
</p>
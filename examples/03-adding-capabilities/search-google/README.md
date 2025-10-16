# Search Google for Answers

> "When users ask questions, I need to search the web for current information"

## 🚀 Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "search_agent" from the dropdown
# Ask questions that need current information!
```

## 📋 The Problem

Your agent needs to answer questions with current, accurate information from the web. Without search capability, it can only provide information from its training data, which may be outdated or incomplete.

## ✅ The Solution

Add Google Search as a tool to your agent. This gives it the ability to:
- Find current information (news, events, updates)
- Research topics beyond its training data
- Verify facts with multiple sources
- Provide citations for its answers

## 💻 Complete Code

```python
from google.adk import Agent
from google.adk.tools.google_search_tool import google_search

# An agent that can search Google and answer questions based on results
root_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    description="An agent that can search Google and answer questions with current information",
    instruction="""You are a helpful research assistant with access to Google search.

    When users ask questions:
    1. Search Google for relevant, current information
    2. Synthesize the search results into a clear, comprehensive answer
    3. Cite your sources when providing information
    4. If you can't find relevant information, say so honestly

    Be thorough but concise in your responses.""",
    tools=[google_search]  # This gives the agent access to Google search
)
```

## 🧪 Try It Out

### Prerequisites

1. **Google Search API Setup** (if using custom search):
   ```bash
   # In your .env file:
   GOOGLE_API_KEY=your-api-key-here
   # Optional: For custom search engine
   GOOGLE_SEARCH_API_KEY=your-search-api-key
   GOOGLE_SEARCH_ENGINE_ID=your-search-engine-id
   ```

   > **Note**: The basic `google_search` tool works with your regular `GOOGLE_API_KEY`. Custom search configuration is optional for more control.

2. **Install ADK**:
   ```bash
   pip install google-adk
   ```

### Sample Queries to Try

Ask your agent questions that require current information:

- **Current Events**: "What happened in tech news this week?"
- **Stock Prices**: "What's the current price of Google stock?"
- **Weather**: "What's the weather forecast for San Francisco?"
- **Recent Sports**: "Who won the latest NBA championship?"
- **Product Info**: "What are the specs of the latest iPhone?"
- **Research Topics**: "What are the latest developments in quantum computing?"

### Example Interaction

```
You: What are the latest features in Python 3.13?

Agent: I'll search for information about Python 3.13's latest features.

[Searching Google...]

Based on my search results, Python 3.13 (released in October 2024) includes several significant features:

1. **Free-threaded CPython**: An experimental build that allows true parallelism by removing the Global Interpreter Lock (GIL)...

2. **Improved Error Messages**: Even better error reporting with more helpful suggestions...

3. **Performance Improvements**: Continued optimizations making Python faster...

Sources:
- Python.org official release notes
- PEP 703 (Making the GIL Optional)
- Python Enhancement Proposals
```

## 📚 What You'll Learn

- ✅ **Adding Tools**: How to give agents new capabilities through tools
- ✅ **Tool Integration**: The `tools` parameter accepts a list of functions
- ✅ **Google Search API**: Using ADK's built-in Google search integration
- ✅ **Information Synthesis**: Writing instructions for research tasks

## 🔧 Customize It

### Add Search Limits

```python
instruction="""...

    Search guidelines:
    - Limit searches to 3 queries maximum per request
    - Focus on authoritative sources (.gov, .edu, established news sites)
    - Prefer recent information (last 6 months) for current events
    """
```

### Specialize for Different Domains

```python
# For technical research:
instruction="You are a technical research assistant. Search for programming tutorials, documentation, and Stack Overflow answers."

# For news aggregation:
instruction="You are a news analyst. Search for multiple news sources and provide balanced coverage of current events."

# For shopping assistant:
instruction="You are a shopping assistant. Search for product reviews, prices, and availability across different retailers."
```

### Combine with Other Tools

```python
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.code_execution_tool import code_execution_tool

tools=[google_search, code_execution_tool]  # Can search AND run code!
```

## 🚨 Common Issues

### Issue: "Search not returning results"
**Solution**:
- Check your API key is valid
- Ensure you have internet connectivity
- Try simpler search queries

### Issue: "Rate limit exceeded"
**Solution**:
- Add delays between searches in your instructions
- Use more specific search queries
- Consider caching results for repeated queries

### Issue: "Outdated information"
**Solution**:
- Instruct the agent to look for recent dates in search results
- Ask for information from the last week/month specifically

## 🎯 Best Practices

1. **Clear Search Intent**: Help the agent understand what to search for
   ```
   Good: "Find the current CEO of OpenAI"
   Better: "Search for who is currently serving as OpenAI's CEO as of 2024"
   ```

2. **Source Verification**: Instruct the agent to cite sources
   ```python
   instruction="Always mention the source website and date of information"
   ```

3. **Fallback Behavior**: Handle cases when search fails
   ```python
   instruction="If search returns no results, explain what you tried to find and suggest alternative queries"
   ```

## ➡️ Next Steps

Now that your agent can search the web, try these enhancements:

- **Call APIs**: See [`call-rest-api`](../call-rest-api) to integrate with specific APIs
- **Process Results**: See [`execute-code`](../execute-code) to analyze search data
- **Multi-Agent Search**: See [`parallel-research`](../../04-orchestrating-agents/parallel-research) for concurrent searches
- **Store Results**: See [`persist-to-firestore`](../../05-managing-context/persist-to-firestore) to save search history

## 📖 Learn More

- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/introduction)
- [ADK Tools Documentation](https://github.com/google/adk/blob/main/docs/tools.md)
- [Web Search Best Practices](https://developers.google.com/search/docs/fundamentals/do-i-need-seo)

---

**Source**: This example is adapted from the official `google_search_agent` sample in the ADK repository.
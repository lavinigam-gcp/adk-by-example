# Create Your First Agent

> "When I'm new to ADK, I need a working agent in seconds"

## 🚀 Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "first_agent" from the dropdown
# Start chatting with your agent!
```

## 📋 The Problem

You're new to ADK and want to see a working agent immediately. You need to understand the absolute minimum required to create a functional agent before diving into complex features.

## ✅ The Solution

This example shows the three essential components of any ADK agent:
1. **Import ADK**: `from google.adk import Agent`
2. **Create an agent**: Define it with a model and instruction
3. **Export as root_agent**: ADK looks for this variable

## 💻 Complete Code

```python
from google.adk import Agent

# This is your first agent!
# It uses Google's Gemini model to have conversations.
root_agent = Agent(
    model="gemini-2.5-flash",  # The AI model to use
    name="first_agent",         # A friendly name for your agent
    instruction="""You are a helpful assistant.
    Answer questions clearly and concisely.
    Be friendly and professional."""
)
```

That's it! In just 8 lines of code, you have a working AI agent.

## 🧪 Try It Out

### Prerequisites
1. Make sure you have ADK installed:
   ```bash
   pip install google-adk
   ```

2. Set your API key in the `.env` file (copy from `.env.example`):
   ```bash
   GOOGLE_API_KEY=your-gemini-api-key-here
   ```

### Run the Agent
1. Navigate to the examples directory
2. Run `adk web`
3. Select "first_agent" from the dropdown
4. Try these sample conversations:
   - "Hello! What can you help me with?"
   - "Explain what an AI agent is in simple terms"
   - "What's the weather like?" (Note: It won't know - we haven't added tools yet!)

## 📚 What You'll Learn

- ✅ **Minimal Setup**: An ADK agent needs just three things
- ✅ **Model Selection**: We use `gemini-2.5-flash` for fast, efficient responses
- ✅ **Instructions Matter**: The instruction defines your agent's personality and behavior
- ✅ **root_agent Convention**: ADK always looks for a variable named `root_agent`

## 🔧 Customize It

### Change the Personality
Edit the instruction to create different types of assistants:

```python
# For a technical expert:
instruction="You are a technical expert. Provide detailed, accurate technical information."

# For a creative writer:
instruction="You are a creative writer. Generate engaging and imaginative responses."

# For a tutor:
instruction="You are a patient tutor. Explain concepts step-by-step with examples."
```

### Change the Model
For more complex tasks, use the pro model:

```python
model="gemini-2.5-pro"  # More capable but slightly slower
```

## 🚨 Common Issues

### Issue: "No API key found"
**Solution**: Make sure you've:
1. Copied `.env.example` to `.env`
2. Added your actual API key (get one free at https://aistudio.google.com/app/apikey)

### Issue: "Agent not showing in dropdown"
**Solution**: Ensure you're running `adk web` from the `examples/` directory, not from this folder

### Issue: "Import error for google.adk"
**Solution**: Install ADK with `pip install google-adk`

## ➡️ Next Steps

Now that you have a basic agent working, try these examples to add more capabilities:

- **Add conversation memory**: See [`chat-with-history`](../../05-managing-context/chat-with-history) to maintain context
- **Add tools**: See [`search-google`](../../03-adding-capabilities/search-google) to let your agent search the web
- **Use configuration**: See [`use-config-yaml`](../use-config-yaml) for no-code agent setup
- **Understand the details**: See [`understand-basics`](../understand-basics) for a fully commented version

## 📖 Learn More

- [Official ADK Documentation](https://github.com/google/adk)
- [Gemini API Documentation](https://ai.google.dev/)
- [ADK Python Reference](https://github.com/google/adk/blob/main/docs/python-reference.md)

---

**Source**: This example is adapted from the official `hello_world` sample in the ADK repository, simplified for beginners.
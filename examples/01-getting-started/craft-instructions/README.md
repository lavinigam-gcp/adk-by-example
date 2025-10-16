# Craft Effective Instructions

> "When my agent gives wrong responses, I need to write better instructions"

## =€ Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "craft_instructions" from the dropdown
# Ask about instruction best practices!
```

## =Ë The Problem

Your agent isn't behaving as expected. It gives vague answers, goes off-topic, or doesn't follow the format you want. The issue isn't the model - it's the instructions. Clear, specific instructions are the difference between a frustrating agent and a helpful one.

##  The Solution

This example demonstrates multiple instruction patterns:
1. **Simple Instructions** - Basic but limited
2. **Detailed Instructions** - Role, responsibilities, and constraints
3. **Example-Driven** - Teaching through demonstration
4. **Format-Specific** - Enforcing output structure
5. **Comprehensive** - Combining all techniques

## =» Instruction Patterns

### Pattern 1: Simple (Avoid This)
```python
instruction="You are a helpful assistant."
```
L Too vague - the agent doesn't know what kind of help to provide

### Pattern 2: Role-Based with Constraints (Recommended)
```python
instruction="""You are a professional customer support agent.

Your responsibilities:
- Answer questions about orders and shipping
- Be polite and solution-oriented
- Provide step-by-step guidance

Important constraints:
- Never share personal information
- If unsure, admit it and escalate
- Keep responses concise"""
```
 Clear role, specific tasks, defined boundaries

### Pattern 3: Example-Driven
```python
instruction="""When explaining concepts, follow this pattern:
1. Simple definition
2. Real-world analogy
3. Practical example

For example, if asked about "API":
- Definition: A way for programs to talk
- Analogy: Like a restaurant menu
- Example: Weather apps using forecast APIs"""
```
 Shows exactly what you want through examples

### Pattern 4: Format-Specific
```python
instruction="""Format responses as:
## Summary
[Overview]

## Key Points
- [Bullet points]

## Recommendations
[Next steps]"""
```
 Ensures consistent, structured output

## >ê Try It Out

### Test Different Instruction Styles

1. **Run the agent**:
   ```bash
   adk web
   # Select "craft_instructions"
   ```

2. **Ask about instruction patterns**:
   - "What makes a good agent instruction?"
   - "Show me examples of poor vs good instructions"
   - "How do I make my agent more consistent?"
   - "What are common instruction mistakes?"

3. **Compare the sub-agents** (if implementing multiple):
   - Try the same question with different instruction styles
   - See how instructions shape responses

## =Ú What You'll Learn

-  **Specificity Matters**: Vague instructions = vague responses
-  **Structure Helps**: Organized instructions lead to organized outputs
-  **Examples Teach**: Showing is better than telling
-  **Constraints Guide**: Clear boundaries prevent unwanted behavior
-  **Tone Shapes Personality**: Instructions define how your agent "sounds"

## =' Best Practices

### DO's 
```python
# Be specific about the role
instruction="You are a Python tutor for beginners..."

# Include examples
instruction="...For instance, when explaining loops, start with..."

# Set clear boundaries
instruction="...Never write code that could be harmful..."

# Define output format
instruction="...Structure your response with numbered steps..."
```

### DON'Ts L
```python
# Too vague
instruction="Help users"

# No context
instruction="Answer questions"

# Missing constraints
instruction="Write code"

# Unclear expectations
instruction="Be helpful and nice"
```

## =¨ Common Issues

### Issue: Agent gives inconsistent responses
**Solution**: Add format specifications and examples to your instructions

### Issue: Agent goes off-topic
**Solution**: Add constraints like "Only discuss [specific topics]"

### Issue: Agent is too verbose/brief
**Solution**: Specify response length: "Keep responses under 3 sentences"

### Issue: Wrong tone or style
**Solution**: Define tone explicitly: "Be professional but approachable"

## ¡ Next Steps

Now that you understand instructions, explore:

- **Configure model parameters**: See [`configure-model`](../configure-model) to control temperature and tokens
- **Use YAML for instructions**: See [`use-yaml-config`](../use-yaml-config) for config-based setup
- **Structure output data**: See [`structure-output`](../structure-output) for JSON responses

## =Ö Learn More

- [ADK Agent Documentation](https://github.com/google/adk/docs/agents.md)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Gemini Best Practices](https://ai.google.dev/docs/gemini_prompting_guide)

---

**Source**: Instruction patterns extracted from multiple ADK samples including hello_world, multi_agent examples, and core_basic_config.
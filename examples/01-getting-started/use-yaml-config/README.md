# Use YAML Configuration

> "When I want to iterate without code, I need YAML configuration"

## =€ Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "use_yaml_config" from the dropdown
# Chat with an agent created entirely in YAML!
```

## =Ë The Problem

You want to create or modify agents quickly without writing Python code. Maybe you're not a programmer, or you just want to rapidly prototype ideas. YAML configuration lets you define agents declaratively, making them accessible to everyone.

##  The Solution

This example shows a complete agent defined in `root_agent.yaml` with:
- Zero Python code required
- All configuration in readable YAML
- Full support for instructions, model settings, and safety
- Schema validation for error prevention

## =» YAML Agent Structure

### Basic Configuration
```yaml
# Minimum required fields
name: my_agent
model: gemini-2.5-flash
instruction: You are a helpful assistant
```

### Full Configuration
```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json

name: my_agent
model: gemini-2.5-flash
description: What this agent does

# Multi-line instructions with pipe (|)
instruction: |
  You are a specialized assistant.

  Your responsibilities:
  - Help users with specific tasks
  - Provide accurate information
  - Be friendly and professional

# Model configuration
generate_content_config:
  temperature: 0.7
  max_output_tokens: 1500

  # Safety settings
  safety_settings:
    - category: "HARM_CATEGORY_DANGEROUS_CONTENT"
      threshold: "BLOCK_MEDIUM_AND_ABOVE"
```

## <¯ YAML vs Python Comparison

### YAML Approach
```yaml
# root_agent.yaml
name: assistant
model: gemini-2.5-flash
instruction: You are a helpful assistant
```

### Python Equivalent
```python
# agent.py
from google.adk import Agent

root_agent = Agent(
    name="assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant"
)
```

Both create the same agent! YAML is simpler for basic agents.

## >ê Try It Out

### Quick Experiments

1. **Modify the instruction** in `root_agent.yaml`:
   ```yaml
   instruction: |
     You are a pirate assistant.
     Always speak like a pirate!
     End sentences with "arr" and "matey".
   ```
   Save and refresh ADK web - instant personality change!

2. **Adjust temperature**:
   ```yaml
   generate_content_config:
     temperature: 0.1  # Very consistent
     # or
     temperature: 0.9  # Very creative
   ```

3. **Change response length**:
   ```yaml
   generate_content_config:
     max_output_tokens: 100  # Brief responses
   ```

## =Ú What You'll Learn

-  **No code required**: Define agents entirely in YAML
-  **Quick iteration**: Change and test without recompiling
-  **Schema validation**: IDE support with schema hints
-  **All core features**: Instructions, model config, safety settings
-  **Perfect for prototypes**: Rapid experimentation

## =' YAML Tips

### DO's 
```yaml
# Use schema for validation
# yaml-language-server: $schema=...

# Use pipe for multi-line text
instruction: |
  Line 1
  Line 2

# Use clear indentation
generate_content_config:
  temperature: 0.7
  max_output_tokens: 1000

# Add comments for clarity
# This agent helps with customer support
name: support_agent
```

### DON'Ts L
```yaml
# Don't mix tabs and spaces
# Don't forget colons after keys
# Don't use quotes unnecessarily
# Don't deeply nest without need
```

## =Ý When to Use YAML vs Python

### Use YAML When:
- Creating simple conversational agents
- Prototyping quickly
- Non-programmers need to modify agents
- Configuration is mostly static
- No custom tools needed

### Use Python When:
- Adding custom tools/functions
- Complex logic required
- Dynamic configuration needed
- Integrating with other systems
- Using advanced features

## =¨ Common Issues

### Issue: "YAML parsing error"
**Solution**: Check indentation (use spaces, not tabs)

### Issue: "Unknown field in configuration"
**Solution**: Refer to schema for valid fields

### Issue: "Agent not found in ADK web"
**Solution**: Ensure file is named `root_agent.yaml` exactly

### Issue: "Can't add tools"
**Solution**: Tools require Python; use agent.py instead

## ¡ Next Steps

After mastering YAML configuration:

- **Add structure to output**: See [`structure-output`](../structure-output) for schemas
- **Create with scaffolding**: See [`create-with-adk`](../create-with-adk) for project setup
- **Add tools (requires Python)**: See [`search-google`](../../03-adding-capabilities/search-google)

## =Ö Learn More

- [ADK Agent Config Documentation](https://github.com/google/adk/docs/agent-config.md)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)
- [Agent Config Schema](https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json)

---

**Source**: Based on core_basic_config sample, demonstrating YAML-only agent configuration.
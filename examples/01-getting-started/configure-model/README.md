# Configure Model Parameters

> "When I need specific output behavior, I need to tune model parameters"

## =€ Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "configure_model" from the dropdown
# Ask about temperature, tokens, or safety settings!
```

## =Ë The Problem

Your agent works, but you need more control over its behavior. Sometimes responses are too creative when you need facts, too long when you need brevity, or too risky when you need safety. Model configuration parameters give you fine-grained control.

##  The Solution

This example demonstrates key model configuration options:
1. **Temperature** - Control randomness/creativity
2. **Max Output Tokens** - Limit response length
3. **Safety Settings** - Filter harmful content
4. **Response MIME Type** - Structure output format

## =» Configuration Examples

### Temperature Control

```python
from google.genai import types

# Creative writing (high temperature)
creative_config = types.GenerateContentConfig(
    temperature=0.9  # Very creative, varied responses
)

# Technical documentation (low temperature)
precise_config = types.GenerateContentConfig(
    temperature=0.1  # Consistent, deterministic responses
)

# Balanced conversation (medium temperature)
balanced_config = types.GenerateContentConfig(
    temperature=0.5  # Natural but reliable
)
```

### Output Length Control

```python
# Brief responses
brief_config = types.GenerateContentConfig(
    max_output_tokens=200  # Twitter-like brevity
)

# Detailed explanations
detailed_config = types.GenerateContentConfig(
    max_output_tokens=2000  # Room for comprehensive answers
)
```

### Safety Settings

```python
# Family-friendly content
safe_config = types.GenerateContentConfig(
    safety_settings=[
        types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="BLOCK_LOW_AND_ABOVE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="BLOCK_MEDIUM_AND_ABOVE"
        )
    ]
)
```

### Structured Output

```python
# JSON responses
json_config = types.GenerateContentConfig(
    temperature=0.2,  # Low temp for consistent structure
    response_mime_type="application/json"
)
```

## <š Parameter Guide

### Temperature (0.0 - 1.0)

| Value | Use Case | Behavior |
|-------|----------|----------|
| 0.0-0.2 | Code generation, facts | Highly deterministic |
| 0.3-0.5 | Documentation, tutorials | Consistent but natural |
| 0.5-0.7 | General assistance | Balanced creativity |
| 0.8-1.0 | Creative writing, brainstorming | Highly creative |

### Max Output Tokens

| Tokens | Use Case | Approximate Length |
|--------|----------|-------------------|
| 50-200 | Brief answers | 1-2 sentences |
| 200-500 | Short responses | 1 paragraph |
| 500-1500 | Standard responses | 2-4 paragraphs |
| 1500-4000 | Detailed explanations | Full articles |

### Safety Thresholds

| Threshold | Description | Use Case |
|-----------|-------------|----------|
| BLOCK_NONE | No filtering | Research, adult content |
| BLOCK_LOW_AND_ABOVE | Strict filtering | Educational, children |
| BLOCK_MEDIUM_AND_ABOVE | Moderate filtering | General audience |
| BLOCK_HIGH_AND_ABOVE | Minimal filtering | Professional content |

## >ê Try It Out

### Experiment with Different Configs

1. **Test temperature effects**:
   - "Write a story about a robot" (try with temp 0.1 vs 0.9)
   - "What is 2+2?" (should be same regardless of temperature)

2. **Test token limits**:
   - "Explain quantum computing" (with max_tokens=100 vs 2000)
   - "Define API" (brief should be sufficient)

3. **Test safety settings**:
   - Ask about sensitive topics with different thresholds
   - Notice how responses change with safety levels

## =Ú What You'll Learn

-  **Temperature affects creativity**: Lower = consistent, Higher = creative
-  **Token limits control verbosity**: Set based on your UI constraints
-  **Safety settings protect users**: Essential for public-facing agents
-  **Response format matters**: JSON mode for structured data extraction
-  **Combine parameters**: Temperature + tokens + safety work together

## =' Best Practices

### DO's 
- Use low temperature (0.1-0.3) for factual/technical content
- Set appropriate token limits for your use case
- Configure safety settings for your audience
- Test different temperatures to find the sweet spot

### DON'Ts L
- Don't use high temperature for financial/medical advice
- Don't set tokens too low for complex explanations
- Don't disable safety settings for public agents
- Don't use temperature 0.0 (can cause repetition)

## =¨ Common Issues

### Issue: Responses are inconsistent
**Solution**: Lower the temperature to 0.1-0.3

### Issue: Responses are too repetitive
**Solution**: Increase temperature slightly (avoid 0.0)

### Issue: Responses get cut off
**Solution**: Increase max_output_tokens

### Issue: Agent refuses safe content
**Solution**: Adjust safety threshold to BLOCK_MEDIUM_AND_ABOVE

## ¡ Next Steps

Now that you can configure models:

- **Structure your output**: See [`structure-output`](../structure-output) for JSON schemas
- **Use YAML configuration**: See [`use-yaml-config`](../use-yaml-config) to set these in YAML
- **Add tools to your agent**: See [`search-google`](../../03-adding-capabilities/search-google)

## =Ö Learn More

- [Gemini API Parameters](https://ai.google.dev/docs/parameters)
- [Safety Settings Guide](https://ai.google.dev/docs/safety_settings)
- [Token Counting](https://ai.google.dev/docs/tokens)

---

**Source**: Configuration patterns from core_generate_content_config_config and multiple ADK samples using GenerateContentConfig.
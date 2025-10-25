## Description

Brief description of your example and what problem it solves.

## Example Details

- **Category**: [e.g., 03-adding-capabilities]
- **Example Name**: [your-example-name]
- **JTBD**: "When [situation], I need to [task], so I can [outcome]"
- **Based on**: [official ADK sample name from .adk/adk-python-code-samples.xml]
- **Difficulty**: [beginner/intermediate/advanced]

## Checklist

Please verify all items before submitting:

### Content Quality
- [ ] Example solves a real, specific problem
- [ ] JTBD statement is clear and user-focused
- [ ] Code is based on official ADK samples
- [ ] README follows the template structure

### Technical Requirements
- [ ] Uses `gemini-2.5-flash` or `gemini-2.5-pro` (unless model integration example)
- [ ] All required files present (`__init__.py`, `agent.py`, `metadata.json`, `README.md`)
- [ ] `language` field in metadata.json
- [ ] `tech_stack` array properly formatted
- [ ] Agent exports `root_agent` variable

### Testing
- [ ] Tested with `adk web` and works correctly
- [ ] Validation script passes 100% (`python scripts/validate_examples.py`)
- [ ] No API keys or secrets in code
- [ ] Example works out of the box with `.env` setup

### Documentation
- [ ] README includes all required sections
- [ ] Sample queries provided
- [ ] Related examples linked (if applicable)

## Testing

Describe how you tested this example:

```bash
# Example:
cd examples
adk web
# Selected "your-example" and tested with:
# - Query 1: ...
# - Query 2: ...
```

## Validation Output

Paste the output of `python scripts/validate_examples.py`:

```
# Paste validation output here
```

## Screenshots (optional)

If helpful, add screenshots showing the example in action.

## Additional Context

Any additional information that would help reviewers understand your contribution.

---

Thank you for contributing to ADK by Example! 🚀

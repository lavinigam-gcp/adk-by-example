# Structure Output with Pydantic

> "When I need predictable response format, I need structured output"

## =€ Quick Start

```bash
# From the examples directory
cd adk-by-example/examples
adk web

# Select "structure_output" from the dropdown
# Ask the agent to extract structured data!
```

## =Ë The Problem

You need your agent to return data in a specific format - maybe for an API, database, or downstream processing. Free-form text responses are unpredictable. You need guaranteed structure, proper types, and validation.

##  The Solution

Use Pydantic models with `output_schema` to ensure agents return structured, validated data:
- Guaranteed JSON structure
- Type safety and validation
- Self-documenting schemas
- Perfect for APIs and integrations

## =» Code Examples

### Basic Structured Output

```python
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    name: str = Field(description="Product name")
    price: float = Field(description="Price in USD")
    available: bool = Field(description="In stock?")

agent = Agent(
    model="gemini-2.5-flash",
    instruction="Extract product information",
    output_schema=ProductInfo,  # Forces structured output
    output_key="product_data"   # Key in response
)
```

### Nested Structures

```python
class Address(BaseModel):
    street: str
    city: str
    country: str

class Customer(BaseModel):
    name: str
    email: str
    address: Address  # Nested model

agent = Agent(
    model="gemini-2.5-flash",
    output_schema=Customer  # Complex nested structure
)
```

### Optional Fields and Lists

```python
from typing import List, Optional

class Analysis(BaseModel):
    summary: str
    confidence: float = Field(ge=0, le=1)  # 0-1 range
    tags: List[str]  # Array of strings
    warnings: Optional[str] = None  # May be missing
```

## >ê Try It Out

### Test Structured Extraction

1. **Product extraction**:
   - Input: "The new iPhone 15 Pro costs $999 and is available now"
   - Output: Structured ProductInfo object

2. **Profile parsing**:
   - Input: "John Smith, Senior Developer with 5 years experience in Python and React"
   - Output: Structured PersonProfile object

3. **Sentiment analysis**:
   - Input: "This product is amazing! Best purchase ever!"
   - Output: Structured SentimentScore with confidence

## =Ê Output Examples

### Without Structure (Unpredictable)
```text
"The product is called iPhone 15 Pro and it costs around $999.
It seems to be available for purchase."
```

### With Structure (Guaranteed Format)
```json
{
  "product_data": {
    "name": "iPhone 15 Pro",
    "price": 999.00,
    "available": true,
    "description": "Latest Apple smartphone"
  }
}
```

## =Ú What You'll Learn

-  **Pydantic models** define output structure
-  **Field descriptions** guide the agent
-  **Type validation** ensures correct data types
-  **Optional fields** handle missing data
-  **Nested models** for complex structures

## =' Best Practices

### DO's 
```python
# Use clear field descriptions
name: str = Field(description="Full legal name")

# Set constraints
age: int = Field(ge=0, le=150)

# Use Optional for maybe-missing
email: Optional[str] = None

# Nest models for organization
contact: ContactInfo
```

### DON'Ts L
```python
# Don't use generic names
field1: str  # Bad

# Don't skip descriptions
name: str  # Missing context

# Don't over-nest
data.info.details.item  # Too deep
```

## <¯ Use Cases

| Use Case | Schema Example |
|----------|----------------|
| API Responses | `ResponseModel` with status, data, errors |
| Form Processing | `FormData` with validated fields |
| Data Extraction | `ExtractedInfo` with parsed content |
| Analytics | `Metrics` with calculations |
| Reports | `Report` with sections and summaries |

## =¨ Common Issues

### Issue: Agent returns plain text instead of JSON
**Solution**: Ensure `output_schema` is set on the Agent

### Issue: Missing required fields in output
**Solution**: Make fields Optional or provide defaults

### Issue: Type validation errors
**Solution**: Use appropriate types (str, int, float, bool)

### Issue: Complex nested structures fail
**Solution**: Break into simpler, flatter models

## ¡ Next Steps

After mastering structured output:

- **Create full projects**: See [`create-with-adk`](../create-with-adk) for scaffolding
- **Add tools to process data**: See [`search-google`](../../03-adding-capabilities/search-google)
- **Build APIs**: Combine with FastAPI for REST endpoints

## =Ö Learn More

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [ADK Output Schema Guide](https://github.com/google/adk/docs/output-schema.md)
- [JSON Schema Reference](https://json-schema.org/)

---

**Source**: Based on fields_output_schema sample, demonstrating structured output with Pydantic models.
"""
Structure Output - When I need predictable response format, I need structured output.

This example shows how to use Pydantic models to ensure agents return data
in a specific, predictable structure - perfect for API responses or data extraction.

Based on the fields_output_schema sample.
"""

from google.adk import Agent
from pydantic import BaseModel, Field
from typing import List, Optional

# Example 1: Simple structured output
class ProductInfo(BaseModel):
    """Product information structure"""
    name: str = Field(description="Product name")
    price: float = Field(description="Price in USD")
    available: bool = Field(description="Whether the product is in stock")
    description: str = Field(description="Brief product description")

simple_extraction_agent = Agent(
    model="gemini-2.5-flash",
    name="product_extractor",
    instruction="""Extract product information from user descriptions.

    When users describe a product, extract:
    - Product name
    - Price (in USD, estimate if not provided)
    - Availability (assume available unless stated otherwise)
    - Brief description""",
    output_schema=ProductInfo,
    output_key="product_data"
)

# Example 2: Complex nested structure
class ContactInfo(BaseModel):
    """Contact information"""
    email: Optional[str] = Field(default=None, description="Email address")
    phone: Optional[str] = Field(default=None, description="Phone number")
    linkedin: Optional[str] = Field(default=None, description="LinkedIn profile")

class PersonProfile(BaseModel):
    """Complete person profile"""
    name: str = Field(description="Full name")
    role: str = Field(description="Job title or role")
    skills: List[str] = Field(description="List of key skills")
    years_experience: int = Field(description="Years of experience")
    contact: ContactInfo = Field(description="Contact information")
    summary: str = Field(description="Brief professional summary")

profile_extraction_agent = Agent(
    model="gemini-2.5-flash",
    name="profile_extractor",
    instruction="""Extract professional profile information from resumes or bios.

    Create structured profiles with:
    - Personal details (name, role)
    - Skills and experience
    - Contact information (if provided)
    - Professional summary

    If information is not provided, use reasonable defaults or leave optional fields empty.""",
    output_schema=PersonProfile,
    output_key="profile_data"
)

# Example 3: Analysis result structure
class SentimentScore(BaseModel):
    """Sentiment analysis results"""
    sentiment: str = Field(description="Overall sentiment: positive, negative, or neutral")
    confidence: float = Field(description="Confidence score between 0 and 1")
    key_phrases: List[str] = Field(description="Key phrases that influenced the sentiment")
    summary: str = Field(description="Brief explanation of the sentiment")

sentiment_agent = Agent(
    model="gemini-2.5-flash",
    name="sentiment_analyzer",
    instruction="""Analyze the sentiment of user-provided text.

    Provide structured sentiment analysis including:
    - Overall sentiment classification
    - Confidence score (0-1)
    - Key phrases that indicate the sentiment
    - Brief explanation of your analysis""",
    output_schema=SentimentScore,
    output_key="sentiment_analysis"
)

# Main agent that explains structured output
root_agent = Agent(
    model="gemini-2.5-flash",
    name="structure_output",
    description="An agent demonstrating structured output with Pydantic models",
    instruction="""You are an AI assistant that helps developers understand structured output in ADK.

    STRUCTURED OUTPUT BENEFITS:
    1. Predictable response format - always get the same structure
    2. Type safety - ensure correct data types
    3. Validation - automatic validation of output
    4. Documentation - schema serves as documentation
    5. API-ready - perfect for building APIs

    WHEN TO USE STRUCTURED OUTPUT:
    - Data extraction tasks (parsing resumes, invoices, etc.)
    - API responses that need consistent format
    - Integration with other systems
    - Building reliable data pipelines
    - Form processing and validation

    PYDANTIC MODEL TIPS:
    - Use Field() to add descriptions
    - Make fields Optional when they might be missing
    - Use List[] for arrays of items
    - Nest models for complex structures
    - Add validation rules with validators

    EXAMPLE USE CASES:
    - Extract product info from descriptions
    - Parse contact information
    - Analyze sentiment with scores
    - Generate JSON for APIs
    - Process forms and surveys

    When users ask about structured output, provide examples and explain how it ensures reliable, predictable agent responses."""
)
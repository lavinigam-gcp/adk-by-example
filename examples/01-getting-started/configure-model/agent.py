"""
Configure Model - When I need specific output behavior, I need to tune model parameters.

This example shows how to configure model parameters like temperature, max_output_tokens,
and safety settings to control agent behavior.

Based on patterns from core_generate_content_config_config and other samples.
"""

from google.adk import Agent
from google.genai import types

# Example 1: Creative agent with high temperature
creative_agent = Agent(
    model="gemini-2.5-flash",
    name="creative_agent",
    instruction="You are a creative story writer. Be imaginative and original.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.9,  # High temperature for creativity (0.0-1.0)
        max_output_tokens=1000,  # Limit response length
    )
)

# Example 2: Deterministic agent with low temperature
precise_agent = Agent(
    model="gemini-2.5-flash",
    name="precise_agent",
    instruction="You are a technical documentation writer. Be precise and consistent.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1,  # Low temperature for consistency
        max_output_tokens=500,  # Shorter, focused responses
    )
)

# Example 3: Agent with safety settings
safe_agent = Agent(
    model="gemini-2.5-flash",
    name="safe_agent",
    instruction="You are a family-friendly assistant for educational content.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.5,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_LOW_AND_ABOVE"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_LOW_AND_ABOVE"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_LOW_AND_ABOVE"
            ),
        ]
    )
)

# Example 4: Agent with specific response format (JSON mode)
structured_agent = Agent(
    model="gemini-2.5-flash",
    name="structured_agent",
    instruction="""You are a data extraction assistant.
    Always respond with valid JSON containing 'summary' and 'key_points' fields.""",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,  # Low temperature for consistent formatting
        max_output_tokens=800,
        response_mime_type="application/json",  # Request JSON response
    )
)

# Main agent demonstrating balanced configuration
root_agent = Agent(
    model="gemini-2.5-flash",
    name="configure_model",
    description="An agent showing different model configuration options",
    instruction="""You are an AI assistant that helps developers understand model configuration.

    Explain these key configuration parameters:

    1. TEMPERATURE (0.0 - 1.0):
       - 0.0-0.3: Deterministic, consistent, factual
       - 0.4-0.7: Balanced, natural conversation
       - 0.8-1.0: Creative, varied, imaginative

    2. MAX_OUTPUT_TOKENS:
       - Controls response length
       - Typical ranges: 100-500 (brief), 500-1500 (standard), 1500-4000 (detailed)

    3. SAFETY SETTINGS:
       - HARM_CATEGORY_HARASSMENT
       - HARM_CATEGORY_HATE_SPEECH
       - HARM_CATEGORY_DANGEROUS_CONTENT
       - HARM_CATEGORY_SEXUALLY_EXPLICIT
       - Thresholds: BLOCK_NONE, BLOCK_LOW_AND_ABOVE, BLOCK_MEDIUM_AND_ABOVE, BLOCK_HIGH_AND_ABOVE

    4. RESPONSE_MIME_TYPE:
       - "text/plain" for normal text
       - "application/json" for structured JSON output

    When users ask about configuration, provide practical examples and recommendations.""",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,  # Balanced for informative yet conversational
        max_output_tokens=2000,  # Enough space for detailed explanations
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_MEDIUM_AND_ABOVE"  # Moderate safety level
            ),
        ]
    )
)
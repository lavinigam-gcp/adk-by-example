"""
First Agent - When I'm new to ADK, I need a working agent in seconds.

This is the simplest possible ADK agent. It shows the three essential components:
1. Import the Agent class from ADK
2. Create an agent with a model and instruction
3. Assign it to root_agent so ADK can find it

Based on the official hello_world sample, simplified for beginners.
"""

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
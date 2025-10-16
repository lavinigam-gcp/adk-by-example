"""
Search Google Agent - When users ask questions, I need to search the web for answers.

This agent can search Google to find current information and answer questions
based on web search results. It demonstrates how to add tools to your agent.

Based on the official google_search_agent sample.
"""

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
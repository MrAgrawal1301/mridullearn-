from crewai import Agent
from crewai.llm import LLM
from langchain_community.llms import OpenAI
from langchain.tools import tool

import os
os.environ["OPENAI_API_KEY"] = "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"


blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=True,
    allow_delegation=False,
    llm=LLM(model="gpt-4o-mini"),
)
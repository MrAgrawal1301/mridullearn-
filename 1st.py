import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel
from agents import blog_agent

class Blog(BaseModel):
    title: str
    content: str


task1 = Task(
    description="""Create a blog title and content on a given {topic}. Make sure the content is under 200 words.""",
    expected_output="A compelling blog title and well-written content.",
    agent=blog_agent,
    output_pydantic=Blog,
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff(inputs={"topic": "B2B"})

# # Option 1: Accessing Properties Using Dictionary-Style Indexing
# print("Accessing Properties - Option 1")
# title = result["title"]
# content = result["content"]
# print("Title:", title)
# print("Content:", content)



# Option 2: Accessing Properties Directly from the Pydantic Model
print("Accessing Properties - Option 2")
title = result.pydantic.title
content = result.pydantic.content
print("Title:", title)
print("Content:", content)

# # Option 3: Accessing Properties Using the to_dict() Method
# print("Accessing Properties - Option 3")
# output_dict = result.to_dict()
# title = output_dict["title"]
# content = output_dict["content"]
# print("Title:", title)
# print("Content:", content)

# # Option 4: Printing the Entire Blog Object
# print("Accessing Properties - Option 5")
# print("Blog:", result)
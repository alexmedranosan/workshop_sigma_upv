import os

from langchain_openai import ChatOpenAI
from agent import Agent
from dotenv import load_dotenv

load_dotenv()

class Narrator:
    def __init__(self, setting="A small village at dawn", model_name="gpt-4o-mini"):
        """
        Initializes the Narrator with an initial setting.

        :param setting: The initial setting of the story.
        :param model_name: The name of the language model to use.
        """
        self.setting = setting
        self.agents = []
        self.langchain_model = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"))  # Initialize Langchain model

    def narrate(self, text):
        """
        Narrates a piece of the story.

        :param text: The text to narrate.
        """
        messages = [
            ("system", "You are a narrator for an interactive story."),
            ("human", text)
        ]
        generated_text = self.langchain_model.invoke(messages).content
        print(generated_text)

    def create_agent(self, name, role, motivation):
        """
        Creates a new agent and adds it to the story.

        :param name: The name of the agent.
        :param role: The role of the agent (e.g., protagonist, antagonist).
        :param motivation: The motivation or goal of the agent.
        :return: The created agent.
        """
        new_agent = Agent(name, role, motivation)
        self.agents.append(new_agent)
        self.narrate(f"A new character named {name}, who is a {role}, has entered the story.")
        return new_agent
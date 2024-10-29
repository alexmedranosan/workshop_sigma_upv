import os

from langchain_openai import ChatOpenAI
from agent import Agent
from dotenv import load_dotenv

load_dotenv()

class Narrator:
    def __init__(self, setting="Un pequeño pueblo al amanecer", model_name="gpt-4o-mini"):
        """
        Initializes the Narrator with an initial setting.

        :param setting: The initial setting of the story.
        :param model_name: The name of the language model to use.
        """
        self.setting = setting
        self.agents = []
        self.langchain_model = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"))
        self.message_history = [
            ("system", f"Eres un narrador que ambienta una historia siendo vívido y atmosférico a la vez que muy muy conciso. El escenario inicial es: '{self.setting}'")
        ]

    def narrate(self, text, choices=False):
        """
        Narrates a piece of the story.

        :param text: The text to narrate.
        :param choices: If False, the generated narrative will focus on descriptive context only.
        """
        if not choices:
            prompt = f"Narra la siguiente escena, pero no incluyas elecciones ni decisiones: '{text}'"
        else:
            prompt = f"Narra la siguiente escena, incluye opciones numeradas: '{text}'"

        self.message_history.append(("human", prompt))
        response = self.langchain_model.invoke(self.message_history)
        generated_text = response.content
        self.message_history.append(("assistant", generated_text))

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
        self.narrate(f"Un nuevo personaje llamado {name}, que es {role}, ha entrado a la historia.", choices=False)
        return new_agent

import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Agent:
    def __init__(self, name, role, motivation, model_name="gpt-4o-mini"):
        """
        Initializes an Agent with a name, role, and motivation.

        :param name: The name of the agent.
        :param role: The role of the agent (e.g., protagonist, antagonist).
        :param motivation: The motivation or goal of the agent.
        """
        self.name = name
        self.role = role
        self.motivation = motivation
        self.langchain_model = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"))
        self.memory = [
            ("system",
             f"Eres {self.name}, un {self.role} cuya motivación es '{self.motivation}'. Recordarás detalles importantes de sus acciones y del contexto.")
        ]

    def take_action(self, action):
        """
        Allows the agent to take an action, which will be narrated by the narrator.

        :param action: The action the agent takes.
        """
        self.memory.append(("human", f"{self.name} realiza la siguiente acción: {action}"))
        print(f"{self.name} decide {action}.")

    def decide_action(self, context):
        """
        Allows the agent to decide an action based on the current context.

        :param context: The current context or situation of the story.
        :return: The decided action.
        """
        # Prompt the agent to decide an action based on the context anr return the action number
        self.memory.append(("human", f"Current context: '{context}'"))
        prompt = f"Basándose en tus acciones anteriores y en el contexto actual, decide qué hacer a continuación. Responde únicamente con el número de la opción."
        self.memory.append(("human", prompt))
        action_response = self.langchain_model.invoke(self.memory)
        action = action_response.content
        print(f"{self.name} decide {action}")
        self.memory.append(("assistant", action))

        return action

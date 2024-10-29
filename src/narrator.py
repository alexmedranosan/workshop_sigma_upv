from agent import Agent


class Narrator:
    def __init__(self, setting="A small village at dawn"):
        """
        Initializes the Narrator with an initial setting.

        :param setting: The initial setting of the story.
        """
        self.setting = setting
        self.agents = []

    @staticmethod
    def narrate(text):
        """
        Narrates a piece of the story.

        :param text: The text to narrate.
        """
        print(f"Narrator: {text}")

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
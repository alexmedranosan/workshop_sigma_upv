class Agent:
    def __init__(self, name, role, motivation):
        """
        Initializes an Agent with a name, role, and motivation.

        :param name: The name of the agent.
        :param role: The role of the agent (e.g., protagonist, antagonist).
        :param motivation: The motivation or goal of the agent.
        """
        self.name = name
        self.role = role
        self.motivation = motivation

    def take_action(self, action):
        """
        Allows the agent to take an action, which will be narrated by the narrator.

        :param action: The action the agent takes.
        """
        print(f"{self.name} decides to {action}.")

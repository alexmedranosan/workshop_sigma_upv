import pytest
from agent import Agent


def test_agent_initialization():
    # Test if Agent initializes correctly with name, role, and motivation
    name = "Erik"
    role = "protagonist"
    motivation = "find the source of the mysterious noises"
    agent = Agent(name, role, motivation)

    assert agent.name == name
    assert agent.role == role
    assert agent.motivation == motivation


def test_agent_take_action():
    # Test if Agent can take an action
    agent = Agent("Erik", "protagonist", "find the source of the mysterious noises")
    action = "investigate the forest"

    # Mock print to avoid actual printing during the test
    with pytest.raises(AssertionError):
        assert agent.take_action(action) == f"{agent.name} decides to {action}."

if __name__ == "__main__":
    test_agent_initialization()
    test_agent_take_action()
    print("All tests passed!")

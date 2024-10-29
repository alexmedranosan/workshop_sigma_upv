from narrator import Narrator
from agent import Agent


def test_narrator_initialization():
    # Test if Narrator initializes correctly with a setting
    setting = "A small village at dawn"
    narrator = Narrator(setting, model_name="gpt-4o-mini")
    assert narrator.setting == setting
    assert len(narrator.agents) == 0


def test_narrator_create_agent():
    # Test if Narrator can create an agent and add it to the story
    narrator = Narrator(model_name="gpt-4o-mini")
    agent = narrator.create_agent("Erik", "protagonist", "find the source of the mysterious noises")

    assert isinstance(agent, Agent)
    assert agent.name == "Erik"
    assert agent.role == "protagonist"
    assert agent.motivation == "find the source of the mysterious noises"
    assert len(narrator.agents) == 1


def test_narrator_narrate():
    # Test if Langchain model is used to generate narrative
    narrator = Narrator(model_name="gpt-4o-mini")
    narrator.narrate("The sun rises over the hills.")
    # Since this is an integration with OpenAI, we simply ensure no exceptions occur during execution

if __name__ == "__main__":
    test_narrator_initialization()
    test_narrator_create_agent()
    test_narrator_narrate()
    print("All tests passed!")

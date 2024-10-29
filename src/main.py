from narrator import Narrator


def main():
    # Initialize the narrator with an initial setting
    narrator = Narrator("A small village at dawn")
    narrator.narrate("The village is quiet, with the sun just rising over the hills.")

    # Create the first agent (protagonist)
    protagonist = narrator.create_agent("Erik", "protagonist", "to find the source of the mysterious noises at night")

    # Narrate the next part of the story
    narrator.narrate("Erik hears strange noises coming from the edge of the village.")

    # Agent takes an action
    protagonist.take_action("investigate the source of the noises")

    # Add another agent (antagonist)
    antagonist = narrator.create_agent("Mara", "antagonist", "to keep the village's secrets hidden")
    narrator.narrate("Mara watches Erik from the shadows, determined to stop him from uncovering the truth.")

    # Antagonist takes an action
    antagonist.take_action("follow Erik silently")


if __name__ == "__main__":
    main()

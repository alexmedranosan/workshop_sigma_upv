from narrator import Narrator


def main():
    # Initialize the narrator with an initial setting
    narrator = Narrator("Un pequeño pueblo al amanecer")
    narrator.narrate("El pueblo está tranquilo, con el sol saliendo por las colinas.", choices=False)

    # Create the first agent (protagonist)
    protagonist = narrator.create_agent("Erik", "protagonista", "encontrar el origen de los misteriosos ruidos nocturnos")

    # Narrate the next part of the story
    narrator.narrate("Erik oye ruidos extraños procedentes de las afueras del pueblo.", choices=True)

    # Agent takes an action based on the context
    action = protagonist.decide_action(narrator.message_history)
    narrator.narrate(f"Erik decide {action}.", choices=False)

    # Add another agent (antagonist)
    antagonist = narrator.create_agent("Mara", "antagonista", "mantener ocultos los secretos del pueblo")
    narrator.narrate("Mara observa a Erik desde las sombras, decidida a impedir que descubra la verdad.", choices=True)

    # Antagonist takes an action based on the context
    action = antagonist.decide_action(narrator.message_history)
    narrator.narrate(f"Mara decide {action}.", choices=False)


if __name__ == "__main__":
    main()
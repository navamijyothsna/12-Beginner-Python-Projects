import random

# --- Story Templates ---
stories = {
    "1": {
        "title": "A Day at the Zoo",
        "prompts": [
            ("animal", "noun (animal)"),
            ("adjective1", "adjective"),
            ("verb_ing", "verb ending in -ing"),
            ("food", "noun (food)"),
            ("number", "number"),
            ("place", "noun (place)"),
            ("adjective2", "adjective"),
            ("name", "a name"),
        ],
        "template": (
            "Today I visited the zoo and saw a {adjective1} {animal} that kept {verb_ing} near its enclosure. "
            "It had eaten {number} bowls of {food} for breakfast! A zookeeper named {name} told me the animal "
            "came all the way from {place}. It was the most {adjective2} creature I have ever seen."
        ),
    },
    "2": {
        "title": "The Space Mission",
        "prompts": [
            ("planet", "noun (planet or made-up place)"),
            ("adjective1", "adjective"),
            ("astronaut_name", "a name"),
            ("verb_past", "verb (past tense)"),
            ("number", "number"),
            ("noun", "noun"),
            ("adjective2", "adjective"),
            ("exclamation", "exclamation (e.g. Wow, Yikes)"),
        ],
        "template": (
            "{exclamation}! Commander {astronaut_name} just {verb_past} onto the surface of {planet}. "
            "The landscape was {adjective1} and covered with {number} strange {noun}s. "
            "Mission Control called it a {adjective2} discovery that would change history forever."
        ),
    },
    "3": {
        "title": "The Haunted House",
        "prompts": [
            ("adjective1", "adjective"),
            ("noun1", "noun"),
            ("name", "a name"),
            ("verb_past", "verb (past tense)"),
            ("body_part", "body part"),
            ("adjective2", "adjective"),
            ("animal", "noun (animal)"),
            ("number", "number"),
        ],
        "template": (
            "On a {adjective1} night, {name} {verb_past} into the old house on the hill. "
            "Every {body_part} trembled as a {adjective2} {noun1} appeared from the shadows. "
            "Suddenly, {number} {animal}s burst through the window and the mystery was solved!"
        ),
    },
}


def pick_story():
    print("\n--- MADLIBS ---")
    print("Choose a story:")
    for key, val in stories.items():
        print(f"  {key}. {val['title']}")
    print("  r. Random")

    choice = input("\nEnter choice: ").strip().lower()

    if choice == "r":
        choice = random.choice(list(stories.keys()))
        print(f"Randomly selected: {stories[choice]['title']}")
    elif choice not in stories:
        print("Invalid choice. Picking randomly.")
        choice = random.choice(list(stories.keys()))

    return stories[choice]


def collect_inputs(prompts):
    print("\nFill in the blanks:\n")
    answers = {}
    for key, label in prompts:
        while True:
            val = input(f"  Enter a {label}: ").strip()
            if val:
                answers[key] = val
                break
            print("  (cannot be empty, try again)")
    return answers


def display_story(story, answers):
    print("\n" + "=" * 50)
    print(f"  {story['title'].upper()}")
    print("=" * 50)
    result = story["template"].format(**answers)
    print(f"\n{result}\n")
    print("=" * 50)


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Madlibs!")
    while True:
        story = pick_story()
        answers = collect_inputs(story["prompts"])
        display_story(story, answers)
        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
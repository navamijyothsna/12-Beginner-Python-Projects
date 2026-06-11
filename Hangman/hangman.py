import random

HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

WORDS = {
    "animals":     ["elephant", "giraffe", "penguin", "dolphin", "kangaroo", "cheetah", "crocodile", "flamingo"],
    "countries":   ["brazil", "germany", "australia", "japan", "canada", "egypt", "argentina", "sweden"],
    "programming": ["python", "function", "variable", "loop", "dictionary", "exception", "recursion", "debugging"],
    "fruits":      ["mango", "pineapple", "strawberry", "blueberry", "watermelon", "apricot", "coconut", "papaya"],
}

MAX_WRONG = len(HANGMAN) - 1


def pick_category():
    print("\nChoose a category:")
    categories = list(WORDS.keys())
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat.capitalize()}")
    print(f"  r. Random")

    while True:
        choice = input("\nEnter choice: ").strip().lower()
        if choice == "r":
            return random.choice(categories)
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
        except ValueError:
            pass
        print("  Invalid choice. Try again.")


def play_round(word, category):
    guessed   = set()
    wrong     = set()
    wrong_count = 0

    print(f"\nCategory: {category.capitalize()}")
    print(f"Word: {len(word)} letters\n")

    while wrong_count < MAX_WRONG:
        print(HANGMAN[wrong_count])

        # display word progress
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"\n  Word:   {display}")

        if "_" not in display:
            print(f"\n  You saved him! The word was '{word}'.")
            return True

        if wrong:
            print(f"  Wrong:  {', '.join(sorted(wrong))}  ({MAX_WRONG - wrong_count} left)")

        # get valid guess
        while True:
            guess = input("\n  Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("  Enter a single letter.")
            elif guess in guessed or guess in wrong:
                print("  Already guessed. Try another.")
            else:
                break

        if guess in word:
            guessed.add(guess)
            print(f"  ✓ '{guess}' is in the word!")
        else:
            wrong.add(guess)
            wrong_count += 1
            print(f"  ✗ '{guess}' is not in the word.")

    # final state
    print(HANGMAN[MAX_WRONG])
    print(f"\n  Game over! The word was '{word}'.")
    return False


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Hangman!")

    wins = losses = 0

    while True:
        category = pick_category()
        word     = random.choice(WORDS[category])

        won = play_round(word, category)

        if won:
            wins += 1
        else:
            losses += 1

        print(f"\n  Score — Wins: {wins}  Losses: {losses}")

        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()

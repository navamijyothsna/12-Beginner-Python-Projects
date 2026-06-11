import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock":     "scissors",
    "paper":    "rock",
    "scissors": "paper",
}

SYMBOLS = {
    "rock":     "🪨",
    "paper":    "📄",
    "scissors": "✂️",
}


def get_user_choice():
    print("\n  1. Rock  2. Paper  3. Scissors")
    while True:
        entry = input("  Your choice: ").strip().lower()
        if entry in ("1", "rock"):
            return "rock"
        elif entry in ("2", "paper"):
            return "paper"
        elif entry in ("3", "scissors"):
            return "scissors"
        else:
            print("  Invalid input. Enter 1, 2, 3 or the name.")


def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif BEATS[user] == computer:
        return "user"
    else:
        return "computer"


def display_result(user, computer, winner):
    u = f"{SYMBOLS[user]} {user.capitalize()}"
    c = f"{SYMBOLS[computer]} {computer.capitalize()}"
    print(f"\n  You: {u}  vs  Computer: {c}")

    if winner == "tie":
        print("  It's a tie!")
    elif winner == "user":
        print(f"  {user.capitalize()} beats {computer}. You win!")
    else:
        print(f"  {computer.capitalize()} beats {user}. Computer wins!")


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Rock Paper Scissors!")

    wins = losses = ties = 0

    while True:
        print("\n--- ROUND ---")
        user     = get_user_choice()
        computer = random.choice(CHOICES)
        winner   = get_winner(user, computer)

        display_result(user, computer, winner)

        if winner == "user":
            wins += 1
        elif winner == "computer":
            losses += 1
        else:
            ties += 1

        print(f"\n  Score — Wins: {wins}  Losses: {losses}  Ties: {ties}")

        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()

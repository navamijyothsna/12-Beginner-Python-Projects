import random


def get_difficulty():
    difficulties = {
        "1": ("Easy",   1,   50,  10),
        "2": ("Medium", 1,  100,   7),
        "3": ("Hard",   1,  200,   5),
    }

    print("\nSelect difficulty:")
    for key, (label, low, high, attempts) in difficulties.items():
        print(f"  {key}. {label:<8} (Range: {low}–{high}, Attempts: {attempts})")
    print("  c. Custom")

    while True:
        choice = input("\nEnter choice: ").strip().lower()
        if choice in difficulties:
            label, low, high, attempts = difficulties[choice]
            print(f"\n{label} selected — guess a number between {low} and {high}.")
            return low, high, attempts
        elif choice == "c":
            return get_custom_range()
        else:
            print("Invalid choice. Try again.")


def get_custom_range():
    while True:
        try:
            low  = int(input("Enter lower bound: "))
            high = int(input("Enter upper bound: "))
            if low >= high:
                print("Upper bound must be greater than lower bound.")
                continue
            attempts = int(input("Enter number of attempts allowed: "))
            if attempts < 1:
                print("Attempts must be at least 1.")
                continue
            return low, high, attempts
        except ValueError:
            print("Please enter valid integers.")


def play_round(low, high, max_attempts):
    secret = random.randint(low, high)
    attempts_left = max_attempts

    print(f"\nGuess the number between {low} and {high}. You have {max_attempts} attempt(s).\n")

    while attempts_left > 0:
        try:
            guess = int(input(f"  [{attempts_left} left] Your guess: "))
        except ValueError:
            print("  Please enter a valid integer.")
            continue

        if guess < low or guess > high:
            print(f"  Out of range! Guess between {low} and {high}.")
            continue

        attempts_left -= 1

        if guess == secret:
            used = max_attempts - attempts_left
            print(f"\n  Correct! You guessed it in {used} attempt(s).")
            return True
        elif guess < secret:
            print("  Too low!", end="")
        else:
            print("  Too high!", end="")

        if attempts_left > 0:
            print(f"  ({attempts_left} attempt(s) remaining)")
        else:
            print()

    print(f"\n  Out of attempts! The number was {secret}.")
    return False


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Guess the Number!")

    wins = 0
    rounds = 0

    while True:
        low, high, max_attempts = get_difficulty()
        won = play_round(low, high, max_attempts)
        rounds += 1
        if won:
            wins += 1

        print(f"\n  Score: {wins} win(s) out of {rounds} round(s)")

        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
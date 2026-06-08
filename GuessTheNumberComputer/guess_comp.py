import random

def get_range():
    print("\n--- GUESS THE NUMBER (Computer Guesses) ---")
    print("Think of a number and the computer will try to guess it.\n")

    while True:
        try:
            low = int(input("Enter the lower bound: "))
            high = int(input("Enter the upper bound: "))
            if low >= high:
                print("Upper bound must be greater than lower bound. Try again.")
            else:
                return low, high
        except ValueError:
            print("Please enter valid integers.")


def computer_guess(low, high):
    attempts = 0

    print(f"\nThink of a number between {low} and {high}. Press Enter when ready.")
    input()

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1

        print(f"Computer guesses: {guess}")
        print("  h = too high  |  l = too low  |  c = correct")

        while True:
            response = input("Your response: ").strip().lower()
            if response in ("h", "l", "c"):
                break
            print("  Invalid input. Enter h, l, or c.")

        if response == "c":
            print(f"\nThe computer guessed your number in {attempts} attempt(s)!")
            return
        elif response == "h":
            high = guess - 1
        elif response == "l":
            low = guess + 1

    print("\nHmm, something went wrong. Did you change your number? :)")


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Guess the Number!")
    while True:
        low, high = get_range()
        computer_guess(low, high)
        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
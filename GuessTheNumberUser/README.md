# Guess the Number (User Guesses)

A terminal-based guessing game where the **computer** picks a secret number and **you** try to guess it. The game gives hints after every guess — too high or too low — and tracks your attempts. Comes with three built-in difficulty levels and a custom mode so you can set your own range and attempt limit.

---

## How to Run

```
python guess_the_number_user.py
```

No external libraries required.

---

## How to Play

1. Select a difficulty (Easy, Medium, Hard, or Custom)
2. The computer picks a secret number within the range
3. Enter your guess
4. The game tells you if it's too high or too low
5. Keep guessing until you get it right or run out of attempts
6. Your score is tracked across rounds

---

## Difficulty Levels

| Level  | Range  | Attempts |
|--------|--------|----------|
| Easy   | 1–50   | 10       |
| Medium | 1–100  | 7        |
| Hard   | 1–200  | 5        |
| Custom | you set | you set |

In Custom mode, you define the lower bound, upper bound, and number of attempts yourself.

---

## Sample Output

```
Select difficulty:
  1. Easy     (Range: 1–50, Attempts: 10)
  2. Medium   (Range: 1–100, Attempts: 7)
  3. Hard     (Range: 1–200, Attempts: 5)
  c. Custom

Enter choice: 2

Medium selected — guess a number between 1 and 100.

Guess the number between 1 and 100. You have 7 attempt(s).

  [7 left] Your guess: 50
  Too low!  (6 attempt(s) remaining)
  [6 left] Your guess: 75
  Too high!  (5 attempt(s) remaining)
  [5 left] Your guess: 63
  Too low!  (4 attempt(s) remaining)
  [4 left] Your guess: 69

  Correct! You guessed it in 4 attempt(s).

  Score: 1 win(s) out of 1 round(s)
```

---

## Features

- Three built-in difficulty levels with increasing range and tighter attempt limits
- Custom mode — set your own range and attempt count
- Too high / too low hints after every guess
- Out-of-range guess detection — invalid guesses don't consume an attempt
- Attempt counter displayed on every prompt
- Win/loss score tracker across multiple rounds
- Input validation — handles non-integer input gracefully
- Play-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| `random` module | generating the secret number |
| `while` loops | game loop, input retry loop |
| Conditionals | evaluating guess vs secret, hint logic |
| User input & validation | difficulty selection, guess input, custom range |
| Functions | `get_difficulty`, `get_custom_range`, `play_round`, `main` |
| Score tracking | wins and rounds counter across sessions |
| f-strings | dynamic prompts and result messages |
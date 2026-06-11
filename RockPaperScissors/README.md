# Rock Paper Scissors

A terminal-based Rock Paper Scissors game where you play against the computer. The computer picks randomly each round, and the game tracks your wins, losses, and ties across as many rounds as you want to play.

---

## How to Run

```
python rock_paper_scissors.py
```

No external libraries required.

---

## How to Play

1. Each round, choose Rock, Paper, or Scissors
2. Enter either the number or the name of your choice
3. The computer picks randomly
4. The result is displayed with an explanation of who beat what
5. Your score is updated after every round
6. Choose to play again or quit

---

## Input Options

You can enter your choice in either format:

| Input | Choice |
|---|---|
| `1` or `rock` | 🪨 Rock |
| `2` or `paper` | 📄 Paper |
| `3` or `scissors` | ✂️ Scissors |

---

## Sample Output

```
--- ROUND ---

  1. Rock  2. Paper  3. Scissors
  Your choice: 1

  You: 🪨 Rock  vs  Computer: ✂️ Scissors
  Rock beats scissors. You win!

  Score — Wins: 1  Losses: 0  Ties: 0

Play again? (y/n): y

--- ROUND ---

  1. Rock  2. Paper  3. Scissors
  Your choice: paper

  You: 📄 Paper  vs  Computer: 📄 Paper
  It's a tie!

  Score — Wins: 1  Losses: 0  Ties: 1
```

---

## Features

- Accepts input by number or name for convenience
- Computer picks randomly using the `random` module
- Emoji symbols shown for both choices each round
- Result message explains who beat what (e.g. *Rock beats Scissors*)
- Win / Loss / Tie score tracker across all rounds
- Input validation — rejects anything outside the valid choices
- Play-again loop

---

## Rules

| You play | Beats |
|---|---|
| 🪨 Rock | ✂️ Scissors |
| 📄 Paper | 🪨 Rock |
| ✂️ Scissors | 📄 Paper |

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| `random` module | computer's random choice each round |
| Dictionaries | `BEATS` map for win logic, `SYMBOLS` for emoji display |
| Conditionals | determining winner, displaying result |
| `while` loop | game loop and play-again flow |
| User input & validation | choice input with number or name support |
| Functions | `get_user_choice`, `get_winner`, `display_result`, `main` |
| Score tracking | wins, losses, ties counters across rounds |

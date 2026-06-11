# Tic-Tac-Toe AI

A terminal-based Tic-Tac-Toe game with three difficulty levels powered by the **Minimax algorithm**. On Hard mode the computer is completely unbeatable — it evaluates every possible future game state and always picks the optimal move. Easy and Medium modes offer a more forgiving experience for casual play.

---

## How to Run

```
python tic_tac_toe_ai.py
```

No external libraries required.

---

## Difficulty Levels

| Level  | Computer Behaviour |
|--------|--------------------|
| Easy   | Plays randomly every turn |
| Medium | Plays optimally 60% of the time, randomly otherwise |
| Hard   | Full Minimax — always plays the best possible move, unbeatable |

---

## How to Play

1. Select a difficulty level
2. Pick your mark (X or O)
3. Take turns entering a cell number (1–9) to place your mark
4. First to get three in a row — horizontally, vertically, or diagonally — wins
5. If all 9 cells fill up with no winner, it's a draw
6. Score is tracked across rounds

---

## Board Layout

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## Sample Output

```
Difficulty:
  1. Easy   — computer plays randomly
  2. Medium — computer plays smart 60% of the time
  3. Hard   — computer is unbeatable (Minimax)

Enter choice: 3

Pick your mark — X or O: X

  You are X. Computer is O. Difficulty: Hard.

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

  Your turn.
  Your move (1–9): 1

 X | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

  Computer is thinking...
  Computer plays 5.

 X | 2 | 3
---+---+---
 4 | O | 6
---+---+---
 7 | 8 | 9
```

---

## How Minimax Works

Minimax is a recursive algorithm used in two-player games. The AI simulates every possible sequence of moves from the current board state all the way to a terminal state (win, loss, or draw) and assigns a score:

- `+1` — AI wins
- `-1` — Human wins
- `0`  — Draw

The AI maximizes its own score while assuming the human will always minimize it. After evaluating all paths, it picks the move that leads to the best guaranteed outcome — making it impossible to beat on Hard mode. At best, you can force a draw.

---

## Features

- Three difficulty levels: Easy, Medium, Hard
- Unbeatable Minimax AI on Hard mode
- Pick your mark (X or O) each round
- Clean grid board that refreshes after every move
- Duplicate move detection and input validation
- Win/draw/loss score tracker across rounds
- Play-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| Recursion | Minimax algorithm exploring all game states |
| `random` module | Easy mode and Medium mode fallback moves |
| Lists | board state, winning combinations, empty cells |
| `any` / `all` | win condition checking |
| Conditionals | game flow, AI difficulty branching |
| `while` loop | game loop, input validation loop |
| Functions | `minimax`, `best_minimax_move`, `get_ai_move`, `play_round`, `main` |
| Dictionaries | score tracking |

# Tic-Tac-Toe

A terminal-based Tic-Tac-Toe game with two modes — Player vs Computer and Player vs Player. The computer opponent uses a strategy-based AI that tries to win, blocks the player, and falls back to smart positional choices. The board is displayed after every move with a clean grid layout.

---

## How to Run

```
python tic_tac_toe.py
```

No external libraries required.

---

## Game Modes

| Mode | Description |
|---|---|
| Player vs Computer | You play against a strategy-based computer opponent |
| Player vs Player | Two players take turns on the same terminal |

---

## How to Play

1. Choose a game mode
2. In PvC mode, pick your mark (X or O)
3. In PvP mode, enter names for both players
4. Players take turns entering a cell number (1–9) to place their mark
5. First to get three in a row — horizontally, vertically, or diagonally — wins
6. If all 9 cells are filled with no winner, it's a draw
7. Score is tracked across rounds in PvC mode

---

## Board Layout

Cell numbers map to positions like this:

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
Game Mode:
  1. Player vs Computer
  2. Player vs Player

Enter choice: 1

Pick your mark — X or O: X

  You are X. Computer is O.

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

  Your turn.
  Your move (1–9): 5

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

  Computer's turn...
  Computer plays 1.

 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
```

---

## Computer AI Strategy

The computer follows this priority order on every turn:

1. **Win** — take any move that wins the game immediately
2. **Block** — stop the player from winning on their next turn
3. **Center** — take position 5 if available
4. **Corner** — take any available corner (1, 3, 7, 9)
5. **Any cell** — pick randomly from remaining cells

---

## Features

- Two game modes: Player vs Computer and Player vs Player
- Strategy-based computer AI (win → block → center → corner → random)
- Clean grid board that refreshes after every move
- Pick your mark (X or O) in PvC mode
- Custom player names in PvP mode
- Duplicate move detection — taken cells are rejected
- Input validation — handles non-integer and out-of-range input
- Win/draw/loss score tracker in PvC mode
- Play-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| Lists | board state, winning combinations |
| List comprehensions | finding empty cells, checking win conditions |
| `any` / `all` | win condition checking across combinations |
| Conditionals | game flow, AI strategy priority |
| `while` loop | game loop, input validation loop |
| Functions | `make_board`, `display_board`, `check_winner`, `get_computer_move`, `play_round`, `main` |
| `random` module | fallback move for the computer |
| Dictionaries | player names and score tracking |
| String methods | input cleaning and mark validation |

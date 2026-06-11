# Minesweeper

A fully playable terminal-based Minesweeper game with three difficulty presets and a custom mode. Reveals empty regions automatically using flood fill, supports flagging suspected mines, and guarantees the first move is always safe. The board is displayed with row and column numbers for easy navigation.

---

## How to Run

```
python minesweeper.py
```

No external libraries required.

---

## Difficulty Levels

| Level        | Board Size | Mines |
|--------------|------------|-------|
| Beginner     | 9 × 9      | 10    |
| Intermediate | 16 × 16    | 40    |
| Expert       | 16 × 30    | 99    |
| Custom       | you set    | you set |

---

## How to Play

1. Pick a difficulty
2. Enter moves in the format: `action row col`
   - `r 3 4` — reveal the cell at row 3, column 4
   - `f 3 4` — place or remove a flag at row 3, column 4
   - `q`     — quit the current round
3. Reveal all non-mine cells to win
4. Hit a mine and it's game over — all mines are revealed

---

## Board Symbols

| Symbol | Meaning |
|--------|---------|
| `#`    | Unrevealed cell |
| `.`    | Revealed empty cell (no adjacent mines) |
| `1–8`  | Number of mines in adjacent cells |
| 🚩     | Flagged cell |
| 💣     | Mine (shown on game over) |

---

## Sample Output

```
  Mines: 10  |  Flags: 1
       1   2   3   4   5   6   7   8   9
     ------------------------------------
   1 |  .|  .|  .|  .|  1|  #|  #|  #|  # |
   2 |  .|  .|  .|  .|  1|  #|  #|  #|  # |
   3 |  .|  1|  1|  2|  2|  #|  #|  #|  # |
   4 |  1|  2|  #|  #| 🚩|  #|  #|  #|  # |
   5 |  #|  #|  #|  #|  #|  #|  #|  #|  # |

  Actions: r = reveal  |  f = flag/unflag  |  q = quit
  Enter action row col (e.g. r 3 4):
```

---

## Features

- Three difficulty presets and a custom board size option
- Flood fill — revealing an empty cell auto-expands to all connected empty cells and their numbered borders
- Safe first move — if the first reveal hits a mine, the board regenerates until it's safe
- Flag system — mark suspected mines with 🚩, unflag by entering the same cell again
- Mine and flag counter displayed above the board every turn
- All mines revealed on game over
- Input validation — handles invalid actions, out-of-range coordinates, already-revealed cells, and flagged cells
- Win/loss score tracker across rounds
- Play-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| 2D lists | board, visible grid, flags grid |
| Recursion | flood fill for auto-revealing empty regions |
| Sets | tracking mine positions efficiently |
| `random` module | placing mines randomly on the board |
| Nested loops | building the board, counting adjacent mines, rendering display |
| Conditionals | game state checks, action handling |
| Functions | `make_board`, `flood_fill`, `reveal`, `check_win`, `display`, `play_round`, `main` |
| Input validation | action parsing, coordinate range checks |
| Score tracking | wins and losses across rounds |

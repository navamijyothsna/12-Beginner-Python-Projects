# Hangman

A terminal-based Hangman game where you guess letters to reveal a hidden word before the stick figure is fully drawn. Choose from four word categories — Animals, Countries, Programming, and Fruits — or pick randomly. You get 6 wrong guesses before it's game over.

---

## How to Run

```
python hangman.py
```

No external libraries required.

---

## How to Play

1. Pick a word category (or press `r` for random)
2. The word is shown as underscores — one per letter
3. Guess one letter at a time
4. A correct guess reveals the letter in the word
5. A wrong guess adds a body part to the hangman
6. Win by revealing the full word before 6 wrong guesses
7. Score is tracked across rounds

---

## Categories

| # | Category | Sample Words |
|---|---|---|
| 1 | Animals | elephant, flamingo, crocodile |
| 2 | Countries | brazil, australia, sweden |
| 3 | Programming | python, recursion, debugging |
| 4 | Fruits | pineapple, watermelon, papaya |

---

## Sample Output

```
Choose a category:
  1. Animals
  2. Countries
  3. Programming
  4. Fruits
  r. Random

Enter choice: 3

Category: Programming
Word: 9 letters

       -----
       |   |
           |
           |
           |
           |
    =========

  Word:   _ _ _ _ _ _ _ _ _

  Guess a letter: p
  ✓ 'p' is in the word!

       -----
       |   |
           |
           |
           |
           |
    =========

  Word:   _ _ _ _ _ _ _ _ _
  Wrong:  (6 left)

  Guess a letter: z
  ✗ 'z' is not in the word.

       -----
       |   |
       O   |
           |
           |
           |
    =========

  Word:   p _ _ _ _ _ _ _
  Wrong:  z  (5 left)
```

---

## Hangman Stages

The figure builds across 7 stages — one added per wrong guess:

```
Stage 0    Stage 1    Stage 2    Stage 3    Stage 4    Stage 5    Stage 6
  |          |          |          |          |          |          |
  |          O          O          O          O          O          O
  |                     |         /|         /|\        /|\        /|\
  |                               |                    /          / \
```

---

## Features

- 7-stage ASCII hangman that draws progressively
- 4 word categories with 8 words each, plus random selection
- Word progress display with underscores and revealed letters
- Wrong letters listed with remaining attempts shown
- Duplicate guess detection — repeated letters don't count as a turn
- Input validation — only single alphabetic characters accepted
- Win/loss score tracker across rounds
- Play-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| `random` module | picking category and word randomly |
| Lists | hangman ASCII stages, word lists per category |
| Dictionaries | mapping categories to word lists |
| Sets | tracking guessed and wrong letters efficiently |
| `while` loop | game loop, input validation loop |
| String methods | `.join()`, `.isalpha()`, `.strip()`, `.lower()` |
| Functions | `pick_category`, `play_round`, `main` |
| Score tracking | wins and losses across rounds |

# Binary Search

A terminal-based Binary Search explorer with three modes — Demo, Custom, and Compare. Built to understand how Binary Search works under the hood, not just use it. Every search shows a step-by-step trace of how the algorithm narrows down the range with each comparison.

---

## How to Run

```
python binary_search.py
```

No external libraries required.

---

## Modes

| Mode | Description |
|---|---|
| Demo | Generates a random sorted list and traces every step of the search |
| Custom | Enter your own sorted list and search for any value |
| Compare | Runs Binary Search and Linear Search side by side on a large list and compares steps and time |

---

## How to Use

1. Pick a mode (1, 2, or 3)
2. Provide a list size or enter your own list
3. Enter a number to search for
4. The search trace is printed step by step
5. Run again or quit

---

## Sample Output — Demo Mode

```
  Sorted list: [4, 9, 15, 23, 31, 38, 44, 51, 60, 67, 72, 85, 91]
  Enter a number to search for: 38

  Step-by-step trace:
  Step 1: low=0  high=12  mid=6  arr[mid]=44  → ↓ go left
  Step 2: low=0  high=5   mid=2  arr[mid]=15  → ↑ go right
  Step 3: low=3  high=5   mid=4  arr[mid]=31  → ↑ go right
  Step 4: low=5  high=5   mid=5  arr[mid]=38  → ✓ found

  Found 38 at index 5 in 4 step(s).
```

---

## Sample Output — Compare Mode

```
  Searching for 8500 in a sorted list of 10000 numbers...

  Linear Search: index=8499   steps≈8500   time=0.4821 ms
  Binary Search: index=8499   steps=14     time=0.0089 ms

  Binary Search was faster.
```

---

## How Binary Search Works

Binary Search works only on **sorted** lists. It repeatedly halves the search range:

1. Check the middle element
2. If it matches — done
3. If the target is smaller — search the left half
4. If the target is larger — search the right half
5. Repeat until found or the range is empty

For a list of 1,000,000 elements, Binary Search takes at most **20 steps**. Linear Search could take up to 1,000,000.

---

## Features

- Three modes: Demo, Custom, Compare
- Step-by-step trace showing `low`, `high`, `mid`, and direction at each step
- Handles missing values — reports not found with steps taken
- Custom list mode with ascending-order validation
- Compare mode times both algorithms with `time.perf_counter` for precision
- Input validation across all modes
- Run-again loop

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| Binary Search algorithm | `binary_search` — divide and conquer on sorted list |
| Linear Search | `linear_search` — baseline comparison in Compare mode |
| `while` loop | search loop, input validation |
| Lists | sorted array, step trace storage |
| Dictionaries | storing step details (low, high, mid, value) |
| `time` module | measuring execution time with `perf_counter` |
| `random` module | generating random sorted lists and targets |
| Functions | `binary_search`, `linear_search`, `demo_mode`, `compare_mode`, `main` |
| Input validation | list parsing, integer checks, sort order check |

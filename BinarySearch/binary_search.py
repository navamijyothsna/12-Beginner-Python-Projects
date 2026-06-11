import random
import time


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = []

    while low <= high:
        mid = (low + high) // 2
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_val": arr[mid],
        })

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def display_steps(arr, steps, target):
    print("\n  Step-by-step trace:")
    for i, step in enumerate(steps, 1):
        low, high, mid = step["low"], step["high"], step["mid"]
        mid_val = step["mid_val"]
        hint = "✓ found" if mid_val == target else ("↑ go right" if mid_val < target else "↓ go left")
        print(f"  Step {i}: low={low}  high={high}  mid={mid}  arr[mid]={mid_val}  → {hint}")


def demo_mode():
    print("\n--- DEMO MODE ---")
    print("Watch Binary Search work on a sorted list step by step.\n")

    size = 0
    while size < 2:
        try:
            size = int(input("  List size (e.g. 20): "))
            if size < 2:
                print("  Size must be at least 2.")
        except ValueError:
            print("  Enter a valid integer.")

    arr = sorted(random.sample(range(1, size * 5), size))
    print(f"\n  Sorted list: {arr}")

    target = None
    while target is None:
        try:
            target = int(input("  Enter a number to search for: "))
        except ValueError:
            print("  Enter a valid integer.")

    index, steps = binary_search(arr, target)
    display_steps(arr, steps, target)

    if index != -1:
        print(f"\n  Found {target} at index {index} in {len(steps)} step(s).")
    else:
        print(f"\n  {target} not found. Took {len(steps)} step(s).")


def custom_mode():
    print("\n--- CUSTOM LIST MODE ---")
    print("Enter your own sorted list and search for a value.\n")

    while True:
        raw = input("  Enter space-separated integers (e.g. 3 7 12 19 25): ")
        try:
            arr = list(map(int, raw.split()))
            if len(arr) < 2:
                print("  Enter at least 2 numbers.")
                continue
            if arr != sorted(arr):
                print("  List must be sorted in ascending order.")
                continue
            break
        except ValueError:
            print("  Only integers allowed.")

    print(f"\n  Your list: {arr}")

    target = None
    while target is None:
        try:
            target = int(input("  Enter a number to search for: "))
        except ValueError:
            print("  Enter a valid integer.")

    index, steps = binary_search(arr, target)
    display_steps(arr, steps, target)

    if index != -1:
        print(f"\n  Found {target} at index {index} in {len(steps)} step(s).")
    else:
        print(f"\n  {target} not found. Took {len(steps)} step(s).")


def compare_mode():
    print("\n--- COMPARE MODE ---")
    print("Compare Binary Search vs Linear Search speed on a large list.\n")

    size = 0
    while size < 100:
        try:
            size = int(input("  List size (e.g. 10000): "))
            if size < 100:
                print("  Enter at least 100 for a meaningful comparison.")
        except ValueError:
            print("  Enter a valid integer.")

    arr    = list(range(1, size + 1))
    target = random.choice(arr + [-1])  # sometimes pick a missing value

    print(f"\n  Searching for {target} in a sorted list of {size} numbers...\n")

    # linear search
    t1     = time.perf_counter()
    l_idx  = linear_search(arr, target)
    t2     = time.perf_counter()
    linear_time = (t2 - t1) * 1000

    # binary search
    t3     = time.perf_counter()
    b_idx, steps = binary_search(arr, target)
    t4     = time.perf_counter()
    binary_time = (t4 - t3) * 1000

    print(f"  Linear Search: index={l_idx:<6}  steps≈{arr.index(target) + 1 if target in arr else size:<6}  time={linear_time:.4f} ms")
    print(f"  Binary Search: index={b_idx:<6}  steps={len(steps):<6}  time={binary_time:.4f} ms")

    if binary_time < linear_time:
        print(f"\n  Binary Search was faster.")
    else:
        print(f"\n  Times were too close to compare at this scale.")


def pick_mode():
    print("\n--- BINARY SEARCH ---")
    print("  1. Demo      — watch it work step by step on a random list")
    print("  2. Custom    — enter your own sorted list")
    print("  3. Compare   — binary vs linear search on a large list")

    while True:
        choice = input("\nEnter choice: ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("  Enter 1, 2, or 3.")


def play_again():
    return input("\nRun again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Binary Search Explorer!")

    while True:
        choice = pick_mode()

        if choice == "1":
            demo_mode()
        elif choice == "2":
            custom_mode()
        else:
            compare_mode()

        if not play_again():
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    main()

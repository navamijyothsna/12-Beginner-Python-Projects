import random


def make_board(rows, cols, mines):
    board = [[0] * cols for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        mine_positions.add((r, c))

    for r, c in mine_positions:
        board[r][c] = "M"

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "M":
                continue
            board[r][c] = count_adjacent_mines(board, r, c, rows, cols)

    return board, mine_positions


def count_adjacent_mines(board, r, c, rows, cols):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                count += 1
    return count


def make_visible(rows, cols):
    return [["#"] * cols for _ in range(rows)]


def make_flags(rows, cols):
    return [[False] * cols for _ in range(rows)]


def display(visible, flags, rows, cols):
    col_header = "     " + "  ".join(str(c + 1).rjust(2) for c in range(cols))
    print(col_header)
    print("     " + "----" * cols)

    for r in range(rows):
        row_label = str(r + 1).rjust(2)
        cells = []
        for c in range(cols):
            if flags[r][c]:
                cells.append(" 🚩")
            elif visible[r][c] == "#":
                cells.append("  #")
            elif visible[r][c] == "M":
                cells.append(" 💣")
            elif visible[r][c] == 0:
                cells.append("  .")
            else:
                cells.append(f"  {visible[r][c]}")
        print(f"  {row_label} |{'|'.join(cells)} |")


def flood_fill(board, visible, flags, r, c, rows, cols):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if visible[r][c] != "#" or flags[r][c]:
        return
    visible[r][c] = board[r][c]
    if board[r][c] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                flood_fill(board, visible, flags, r + dr, c + dc, rows, cols)


def reveal(board, visible, flags, r, c, rows, cols):
    if board[r][c] == "M":
        visible[r][c] = "M"
        return "mine"
    flood_fill(board, visible, flags, r, c, rows, cols)
    return "safe"


def check_win(board, visible, mine_positions, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in mine_positions and visible[r][c] == "#":
                return False
    return True


def reveal_all_mines(board, visible, mine_positions):
    for r, c in mine_positions:
        visible[r][c] = "M"


def get_move(rows, cols):
    print("\n  Actions: r = reveal  |  f = flag/unflag  |  q = quit")
    while True:
        raw = input("  Enter action row col (e.g. r 3 4): ").strip().lower().split()
        if len(raw) == 1 and raw[0] == "q":
            return "q", -1, -1
        if len(raw) != 3 or raw[0] not in ("r", "f"):
            print("  Invalid input. Try: r 3 4  or  f 3 4")
            continue
        action = raw[0]
        try:
            r, c = int(raw[1]) - 1, int(raw[2]) - 1
            if 0 <= r < rows and 0 <= c < cols:
                return action, r, c
            print(f"  Row must be 1–{rows}, column must be 1–{cols}.")
        except ValueError:
            print("  Row and column must be integers.")


def pick_difficulty():
    presets = {
        "1": ("Beginner",     9,  9,  10),
        "2": ("Intermediate", 16, 16, 40),
        "3": ("Expert",       16, 30, 99),
    }
    print("\nDifficulty:")
    for key, (label, rows, cols, mines) in presets.items():
        print(f"  {key}. {label:<14} ({rows}x{cols}, {mines} mines)")
    print("  c. Custom")

    while True:
        choice = input("\nEnter choice: ").strip().lower()
        if choice in presets:
            label, rows, cols, mines = presets[choice]
            return rows, cols, mines
        elif choice == "c":
            return pick_custom()
        print("  Enter 1, 2, 3, or c.")


def pick_custom():
    while True:
        try:
            rows  = int(input("  Rows (2–20): "))
            cols  = int(input("  Cols (2–30): "))
            max_m = rows * cols - 1
            mines = int(input(f"  Mines (1–{max_m}): "))
            if 2 <= rows <= 20 and 2 <= cols <= 30 and 1 <= mines <= max_m:
                return rows, cols, mines
            print("  Values out of range. Try again.")
        except ValueError:
            print("  Enter valid integers.")


def play_round():
    rows, cols, mine_count = pick_difficulty()
    board, mine_positions  = make_board(rows, cols, mine_count)
    visible                = make_visible(rows, cols)
    flags                  = make_flags(rows, cols)
    flag_count             = 0
    first_move             = True

    print(f"\n  {rows}x{cols} board — {mine_count} mines. Good luck!\n")

    while True:
        print(f"\n  Mines: {mine_count}  |  Flags: {flag_count}")
        display(visible, flags, rows, cols)

        action, r, c = get_move(rows, cols)

        if action == "q":
            print("  Quitting round.")
            return False

        if action == "f":
            if visible[r][c] != "#":
                print("  Can only flag unrevealed cells.")
                continue
            flags[r][c] = not flags[r][c]
            flag_count += 1 if flags[r][c] else -1
            continue

        # reveal
        if flags[r][c]:
            print("  Unflag the cell first before revealing.")
            continue
        if visible[r][c] != "#":
            print("  Cell already revealed.")
            continue

        # safe first move — regenerate board if first click hits a mine
        if first_move and board[r][c] == "M":
            while board[r][c] == "M":
                board, mine_positions = make_board(rows, cols, mine_count)
            first_move = False

        first_move = False
        result = reveal(board, visible, flags, r, c, rows, cols)

        if result == "mine":
            reveal_all_mines(board, visible, mine_positions)
            print(f"\n  Mines: {mine_count}  |  Flags: {flag_count}")
            display(visible, flags, rows, cols)
            print("\n  💥 BOOM! You hit a mine. Game over.")
            return False

        if check_win(board, visible, mine_positions, rows, cols):
            print(f"\n  Mines: {mine_count}  |  Flags: {flag_count}")
            display(visible, flags, rows, cols)
            print("\n  🎉 You cleared the board. You win!")
            return True


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Minesweeper!")
    wins = losses = 0

    while True:
        won = play_round()
        if won:
            wins += 1
        else:
            losses += 1
        print(f"\n  Score — Wins: {wins}  Losses: {losses}")
        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()

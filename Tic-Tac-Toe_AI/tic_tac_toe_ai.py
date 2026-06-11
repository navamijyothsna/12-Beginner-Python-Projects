import random

WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]


def make_board():
    return [str(i + 1) for i in range(9)]


def display_board(board):
    print()
    for i in range(0, 9, 3):
        row = []
        for cell in board[i:i+3]:
            if cell == "X":
                row.append(" X ")
            elif cell == "O":
                row.append(" O ")
            else:
                row.append(f" {cell} ")
        print("|".join(row))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(board, mark):
    return any(all(board[i] == mark for i in combo) for combo in WINNING_COMBOS)


def check_draw(board):
    return all(cell in ("X", "O") for cell in board)


def empty_cells(board):
    return [i for i, cell in enumerate(board) if cell not in ("X", "O")]


# --- Minimax ---

def minimax(board, is_maximizing, ai_mark, human_mark):
    if check_winner(board, ai_mark):
        return 1
    if check_winner(board, human_mark):
        return -1
    if check_draw(board):
        return 0

    empty = empty_cells(board)

    if is_maximizing:
        best = -2
        for i in empty:
            board[i] = ai_mark
            score = minimax(board, False, ai_mark, human_mark)
            board[i] = str(i + 1)
            best = max(best, score)
        return best
    else:
        best = 2
        for i in empty:
            board[i] = human_mark
            score = minimax(board, True, ai_mark, human_mark)
            board[i] = str(i + 1)
            best = min(best, score)
        return best


def get_ai_move(board, ai_mark, human_mark, difficulty):
    empty = empty_cells(board)

    if difficulty == "easy":
        return random.choice(empty)

    if difficulty == "medium":
        # 60% chance of playing optimally, otherwise random
        if random.random() < 0.6:
            return best_minimax_move(board, ai_mark, human_mark)
        return random.choice(empty)

    # hard — full minimax
    return best_minimax_move(board, ai_mark, human_mark)


def best_minimax_move(board, ai_mark, human_mark):
    empty = empty_cells(board)
    best_score = -2
    best_move  = None

    for i in empty:
        board[i] = ai_mark
        score = minimax(board, False, ai_mark, human_mark)
        board[i] = str(i + 1)
        if score > best_score:
            best_score = score
            best_move  = i

    return best_move


# --- Input helpers ---

def pick_difficulty():
    levels = {"1": "easy", "2": "medium", "3": "hard"}
    print("\nDifficulty:")
    print("  1. Easy   — computer plays randomly")
    print("  2. Medium — computer plays smart 60% of the time")
    print("  3. Hard   — computer is unbeatable (Minimax)")
    while True:
        choice = input("\nEnter choice: ").strip()
        if choice in levels:
            return levels[choice]
        print("  Enter 1, 2, or 3.")


def pick_mark():
    while True:
        mark = input("\nPick your mark — X or O: ").strip().upper()
        if mark in ("X", "O"):
            return mark
        print("  Enter X or O.")


def get_player_move(board):
    while True:
        try:
            move = int(input("  Your move (1–9): "))
            if 1 <= move <= 9 and board[move - 1] not in ("X", "O"):
                return move - 1
            print("  That cell is taken or out of range. Try again.")
        except ValueError:
            print("  Enter a number between 1 and 9.")


# --- Round ---

def play_round(difficulty):
    board       = make_board()
    player_mark = pick_mark()
    ai_mark     = "O" if player_mark == "X" else "X"
    current     = "X"

    print(f"\n  You are {player_mark}. Computer is {ai_mark}. Difficulty: {difficulty.capitalize()}.")

    while True:
        display_board(board)

        if current == player_mark:
            print("  Your turn.")
            move = get_player_move(board)
        else:
            print("  Computer is thinking...")
            move = get_ai_move(board, ai_mark, player_mark, difficulty)
            print(f"  Computer plays {move + 1}.")

        board[move] = current

        if check_winner(board, current):
            display_board(board)
            if current == player_mark:
                print("  You win!")
                return "player"
            else:
                print("  Computer wins!")
                return "computer"

        if check_draw(board):
            display_board(board)
            print("  It's a draw!")
            return "draw"

        current = "O" if current == "X" else "X"


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Tic-Tac-Toe AI!")
    print("\nBoard positions:")
    display_board(make_board())

    scores = {"player": 0, "computer": 0, "draw": 0}

    while True:
        difficulty = pick_difficulty()
        result     = play_round(difficulty)
        scores[result] += 1

        print(f"\n  Score — You: {scores['player']}  Computer: {scores['computer']}  Draws: {scores['draw']}")

        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()

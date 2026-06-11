import random

WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6],             # diagonals
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


def get_player_move(board):
    while True:
        try:
            move = int(input("  Your move (1–9): "))
            if 1 <= move <= 9 and board[move - 1] not in ("X", "O"):
                return move - 1
            else:
                print("  That cell is taken or out of range. Try again.")
        except ValueError:
            print("  Enter a number between 1 and 9.")


def get_computer_move(board, computer_mark, player_mark):
    empty = [i for i, cell in enumerate(board) if cell not in ("X", "O")]

    # win if possible
    for i in empty:
        board[i] = computer_mark
        if check_winner(board, computer_mark):
            board[i] = str(i + 1)
            return i
        board[i] = str(i + 1)

    # block player
    for i in empty:
        board[i] = player_mark
        if check_winner(board, player_mark):
            board[i] = str(i + 1)
            return i
        board[i] = str(i + 1)

    # take center
    if 4 in empty:
        return 4

    # take a corner
    for i in [0, 2, 6, 8]:
        if i in empty:
            return i

    # take any cell
    return random.choice(empty)


def pick_mode():
    print("\nGame Mode:")
    print("  1. Player vs Computer")
    print("  2. Player vs Player")
    while True:
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            return "pvc"
        elif choice == "2":
            return "pvp"
        print("  Enter 1 or 2.")


def pick_mark():
    while True:
        mark = input("\nPick your mark — X or O: ").strip().upper()
        if mark in ("X", "O"):
            return mark
        print("  Enter X or O.")


def play_round(mode):
    board = make_board()

    if mode == "pvc":
        player_mark   = pick_mark()
        computer_mark = "O" if player_mark == "X" else "X"
        print(f"\n  You are {player_mark}. Computer is {computer_mark}.")
        current = "X"

        while True:
            display_board(board)

            if current == player_mark:
                print("  Your turn.")
                move = get_player_move(board)
            else:
                print("  Computer's turn...")
                move = get_computer_move(board, computer_mark, player_mark)
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

    else:  # pvp
        names = {
            "X": input("\n  Name for X player: ").strip() or "Player X",
            "O": input("  Name for O player: ").strip() or "Player O",
        }
        current = "X"

        while True:
            display_board(board)
            print(f"  {names[current]}'s turn ({current}).")
            move = get_player_move(board)
            board[move] = current

            if check_winner(board, current):
                display_board(board)
                print(f"  {names[current]} wins!")
                return names[current]

            if check_draw(board):
                display_board(board)
                print("  It's a draw!")
                return "draw"

            current = "O" if current == "X" else "X"


def play_again():
    return input("\nPlay again? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Tic-Tac-Toe!")
    print("\nBoard positions:")
    display_board(make_board())

    scores = {"player": 0, "computer": 0, "draw": 0}

    while True:
        mode = pick_mode()

        if mode == "pvc":
            result = play_round(mode)
            scores[result] += 1
            print(f"\n  Score — You: {scores['player']}  Computer: {scores['computer']}  Draws: {scores['draw']}")
        else:
            result = play_round(mode)
            print(f"\n  Result: {'Draw' if result == 'draw' else result + ' wins'}")

        if not play_again():
            print("\nThanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()

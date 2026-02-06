# Tic-Tac-Toe Game - Part 4 (Win Detection + Draw Logic)

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_valid_move(row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def make_move(player):
    while True:
        print(f"\nPlayer {player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        if is_valid_move(row, col):
            board[row][col] = player
            break
        else:
            print("Invalid move! Try again.")

def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw():
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    current_player = "X"

    while True:
        print_board()
        make_move(current_player)

        # Check win
        if check_win(current_player):
            print_board()
            print(f"\n🎉 Player {current_player} WINS! 🎉")
            break

        # Check draw
        if is_draw():
            print_board()
            print("\n🤝 It's a DRAW!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()

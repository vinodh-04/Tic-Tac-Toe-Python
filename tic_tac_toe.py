# Tic-Tac-Toe Game - (Game Loop + Turn Switching)

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

def play_game():
    current_player = "X"

    for turn in range(9):   # Maximum 9 moves in Tic-Tac-Toe
        print_board()
        make_move(current_player)

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    print_board()
    print("\nGame Over! (Win/Draw check comes in Part 4)")

# Start the game
play_game()

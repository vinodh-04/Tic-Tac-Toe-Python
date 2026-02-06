# Tic-Tac-Toe Game - Part 2 (Player Input + Validation)

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
    # Check boundaries and empty space
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        return True
    return False

def make_move(player):
    while True:
        print(f"\nPlayer {player}'s turn")

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if is_valid_move(row, col):
            board[row][col] = player
            break
        else:
            print("Invalid move! Try again.")

# ---- Testing Part 2 ----
print_board()

make_move("X")
print_board()

make_move("O")
print_board()

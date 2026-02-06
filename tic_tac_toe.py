# Tic-Tac-Toe Game - Part 1 (Game Board)

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

# Test display
print_board()

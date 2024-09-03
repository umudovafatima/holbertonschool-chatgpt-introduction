#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner.

    Parameters:
    board (list of list of str): The tic-tac-toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """
    Check if the board is full and there's no winner.

    Parameters:
    board (list of list of str): The tic-tac-toe board.

    Returns:
    bool: True if the board is full and there's no winner, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)

def tic_tac_toe():
    """
    Play the tic-tac-toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid coordinates. Please enter values between 0 and 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                if is_draw(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()

import os
import time

# Initial board state
board = [' '] * 10  # Index 0 will be ignored for simplicity
player = 1

# Win Flags
Win = 1
Draw = -1
Running = 0

# Function to draw the game board
def draw_board():
    print("\n" * 100)  # Clear the screen
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")

# Function to check if a position is available
def check_position(x):
    return board[x] == ' '

# Function to check for a win or draw
def check_win():
    # Define winning combinations
    win_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return Win  # Return Win if there's a winner

    if ' ' not in board[1:]:
        return Draw  # Return Draw if the board is full without a winner

    return Running  # Return Running if the game is ongoing

# Game setup
print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
time.sleep(1)

# Main game loop
while True:
    draw_board()

    # Determine current player and mark
    if player % 2 != 0:
        mark = 'X'
    else:
        mark = 'O'

    # Get player's move
    while True:
        try:
            choice = int(input("Player {}'s turn. Enter position (1-9): ".format(player)))
            if 1 <= choice <= 9 and check_position(choice):
                break
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Make the move and check for win/draw
    board[choice] = mark
    game_result = check_win()

    # Game result handling
    if game_result == Win:
        draw_board()
        print("Player {} wins!".format(player))
        break
    elif game_result == Draw:
        draw_board()
        print("It's a draw!")
        break

    # Switch to the other player
    player = 2 if player == 1 else 1
    time.sleep(1)

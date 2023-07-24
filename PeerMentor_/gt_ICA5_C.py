# gt_ICA5_C.py

# Adding exception handling to ICA4_C
# Tic-Tac-Toe

# input: invalid move,
# output: retry move, type of invalidation

# This is a continuation of the tic-tac-toe gameset
# only thing that is really changing is the input validation


#by Gentry Trimble


def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n+---+---+---+")
    # Using a nested for loop to establish the tic-tac-toe board
def check_win(board): # Game logic for wins
    for row in board:
        if row[0] == row[1] == row[2] != ' ': # if straight row then win
            return True
    for col in range(3): # if it is a column win
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] !=" ": # for each diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False # else the game continues
def getVerification(var_):
    while True:  # input validation for rows
        try:
            var = int(input(f"Enter the {var_} (1, 2, 3): "))
        except ValueError:
            print("Invalid or no input. Try again.")
            continue
        else:
            return var


def get_move(board,current_player): # to ensure user imput is correct
    while True:
        print(f"{current_player}'s Turn")
        row = getVerification('row')
        col = getVerification('col')
        if 1 <= row <= 3 and 1 <= col <= 3:
            if board[row - 1][col - 1] == ' ':
                return row, col
            else:
                print("This square is already taken. Try again.")
        else:
            print("Invalid move. Row and column numbers must be between 1 and 3. Try again.")
def play_game(): # actual game matrix,
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # initializes the board
    current_player = "X"
    moves = 0 # move counter
    while True:
        print_board(board)
        print()
        row,col = get_move(board,current_player) # gets player input
        row = row -1
        col = col -1
        print()
        if board[row][col] == " ":
            board[row][col] = current_player
            moves +=1
        else:
            print("Invalid move. Try again")
            continue
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")# uses game rules to find win
            print()
            break
        elif moves == 9: # if there is 9 moves then everything is filled up, if the check win isn't true then it'll be a tie
            print_board(board)
            print("It's a tie!! ")
            print()
            break
        if current_player == "X":
            current_player = "O"
        else: current_player = "X"
def main():
    print("Welcome to Tic-Tac-Toe Game!\n")
    repeat = "y"
    while repeat.lower() == "y":
        play_game()
        repeat = input("Play Again? (y/n) ? ")
    print()
    print("Thank you! Bye!")

if __name__ == '__main__':
    main()

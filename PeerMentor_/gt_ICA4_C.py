#gt_ICA4_C.py
# Two player Tic tac toe game
# inputs:  row/ column for each players turn
# output: x or o on the board, win? tie? loss

# by Gentry Trimble

def print_board(board):
    # General board to be referenced throughout the game, using indicies for placement of x, o
    print("+---+---+---+")
    print("| "+ board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")

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
def get_move(): # to ensure user imput is correct
    while True:
        row = int(input("Enter the row (1,2,3): "))
        col = int(input("Enter the column (1,2,3): "))

        if 0<row<4 and 0<col<4:
            break
        elif 0<row<4:
            if col < 1 or col > 3:
                print("Invalid column number. Try again")
        elif 0 < col < 4:
            if row < 1 or row > 3:
                print("Invalid row number. Try again")




    return row,col
def play_game(): # actual game matrix,
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # initializes the board
    current_player = "X"
    moves = 0 # move counter
    while True:
        print_board(board)
        print()
        print(f"{current_player}'s Turn")
        row,col = get_move() # gets player input
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
        repeat = input("Play again? (y/n) ? ")
    print("Thank you! Bye!")

if __name__ == '__main__':
    main()
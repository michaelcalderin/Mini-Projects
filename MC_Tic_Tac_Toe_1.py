"""
EGN5442 Mini-Project 1

Name: Michael Calderin
UFID: 84670557
Date: 09/30/2024

This program allows users to play Tic Tac Toe. The board is represented as a 2D array
which is of 3x3 size. Player X starts and will be asked where to place their symbol.
Input is validated to ensure it follows a format of row number followed by a comma and
the column number. Extra spaces are acceptable but lack of integer inputs or numbers
that are not within the range of the board will result in a request to try again. If the
spot is already taken then the user will also be prompted to try again. The players will 
take turns making moves until a win (3 symbols are consecutively vertical, horizontal, or 
diagonal) or a draw (full board). At this point, players will be asked if they want to go 
for another game.
"""

def printBoard(board):

    """ Prints the board with dashes as separation """

    # Finding number of rows and columns in the board
    numRows = len(board)
    numCols = len(board[0])

    # Forming the header for the printed board: |R\C| 0 | 1 | 2 |
    header = "|R\\C|"

    for col in range(numCols):
        header += f" {col} |"

    # Forming the dashes that will be used as separations: -----------------
    dashes = ""

    for _ in range(len(header)):
        dashes += "-"

    # Printing header
    print(dashes)
    print(header)
    print(dashes)

    # Printing the board
    for row in range(numRows):
        line = f"| {row} |"

        for col in range(numCols):
            line += f" {board[row][col]} |"

        print(line)
        print(dashes)

def createBoard():

    """ 
    Creates a board represented as a 2D array 
    
    Return:
        2D array (3x3) with empty spaces denoting empty entries
    """

    return [[" " for col in range(3)] for row in range(3)]

def entryToCoordinate(entry):

    """ 
    Tries to convert user entry into a coordinate on the board (row, col)
        
    Return:
        (row, col) if possible
        None if not possible
    """

    # Split the input by comma to try to get [row, col]
    entry = entry.split(",")

    # If input cannot provide a pair for a coordinate then return None
    if len(entry) != 2:
        return None

    # Try to convert user input into a row and column number
    row = -1
    col = -1

    try:
        row = int(entry[0])
        col = int(entry[1])
        return (row, col)

    except ValueError as e:
        return None

def validateEntry(row, col, board):

    """ Verifies if the user's input is a coordinate on the board """

    # Finding number of rows and columns in board
    numRows = len(board)
    numCols = len(board[0])

    # Return True if the spot is on the board, otherwise return False
    if 0 <= row < numRows and 0 <= col < numCols:
        return True

    return False

def checkFull(board):

    """ Checks if the board is full by detecting empty spots """

    # Finding number of rows and columns in board
    numRows = len(board)
    numCols = len(board[0])

    # If empty spot is found then board is not full
    for row in range(numRows):
        for col in range(numCols):
            if board[row][col] == " ":
                return False
            
    return True

def checkWin(row, col, board):

    """ Checks if (row, col) spot on board leads to a win """

    # Finding number of rows and columns in board
    numRows = len(board)
    numCols = len(board[0])

    symbol = board[row][col]
    verticalWin = True
    horizontalWin = True
    diagonalWin = True
    
    # Check for a vertical win
    for i in range(numRows):
        if board[i][col] != symbol:
            verticalWin = False

    # Check for a horizontal win
    for i in range(numCols):
        if board[row][i] != symbol:
            horizontalWin = False

    # Check for a diagonal win
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        diagonalWin = True

    elif board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
        diagonalWin = True

    else:
        diagonalWin = False

    # Return True if there is any type of win
    return True if (verticalWin or horizontalWin or diagonalWin) else False

def main():

    """ 
    Creates an empty board and continuously allows players to make moves until
    a win or draw. Players will then be asked if they want to go again. If they
    do, this system will repeat. Otherwise, the program will terminate.

    Note: Turn 0 refers to player X and turn 1 refers to player O
    """

    # Loop for overall program
    continueProgram = True

    while(continueProgram):

        # Creates board and sets turn to player 0 (turn = {0, 1})
        board = createBoard()
        symbols = ("X", "O")
        turn = 0
        
        # Initial message and board for a new game
        print("New Game: X goes first.")
        print()
        printBoard(board)
        print()

        # Loop for an individual game
        endGame = False

        while(not endGame):

            entry = None
            coord = None

            # Get input from player to see what spot they want to place their symbol in
            while(entry is None):

                # Ask where to put player's symbol
                print(f"{symbols[turn]}'s turn.")
                print(f"Where do you want your {symbols[turn]} placed?")
                print("Please enter row number and column number separated by a comma.")
                entry = input()
                coord = entryToCoordinate(entry)

                # Tell player what they entered (will display "?" for row # and col # if format specified is not followed)
                print(f"You have entered row #{"?" if coord is None else coord[0]}")
                print(f"{"":10}and column #{"?" if coord is None else coord[1]}")

                # If format was not followed or the row/col # is not in the board then ask them to try again
                if (coord is None) or (not validateEntry(coord[0], coord[1], board)):
                    print("Invalid entry: try again.")
                    print("Row & column numbers must be either 0, 1, or 2.")
                    print()
                    entry = None

                # If cell they chose is already taken then ask them to try again
                elif (coord is not None) and (board[coord[0]][coord[1]] != " "):
                    print("That cell is already taken.")
                    print("Please make another selection.")
                    print()
                    entry = None

            # Thank the player for a successful selection and update board
            print("Thank you for your selection.")
            row, col = coord[0], coord[1]
            board[row][col] = symbols[turn]

            # Check if a player has won and ask if they want to go again
            if checkWin(row, col, board):

                print(f"{symbols[turn]} IS THE WINNER!!!")
                printBoard(board)
                print()
                print("Another game? Enter Y or y for yes.")
                anotherGame = input()

                if anotherGame in ["Y", "y"]:
                    endGame = True
                    break
                else:
                    endGame = True
                    continueProgram = False
                    break

            # Check if the board is full (which is a tie) and ask to go again
            elif checkFull(board):

                print()
                print("DRAW! NOBODY WINS!")
                printBoard(board)
                print()
                print("Another game? Enter Y or y for yes.")
                anotherGame = input()

                if anotherGame in ["Y", "y"]:
                    endGame = True
                    break
                else:
                    endGame = True
                    continueProgram = False
                    break

            # Show the current board
            printBoard(board)
            print()

            # Change the turn to the other player
            if turn == 0:
                turn = 1
            else: 
                turn = 0

    # When done with all games, thank the users for playing
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
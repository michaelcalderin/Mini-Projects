"""
EGN5442 Mini-Project 1

Name: Michael Calderin
UFID: 84670557
Date: 09/30/2024

This program allows users to play Connect 4. The board is represented as a 2D array
which is of 6x7 size. Player X starts and will be asked where to place their symbol,
given the list of available positions. Input is validated to ensure a format of 
column-letter and row-number (ex. c1). Extra spaces are acceptable but inputs that 
are not in the list of available positions will result in a request to try again. The 
players will take turns making moves until a win (4 symbols are consecutively vertical, 
horizontal, or diagonal) or a draw (full board). At this point, players will be asked 
if they want to go for another game.
"""

def printBoard(board):

    """ Prints the board with dashes as separation """

    # Finding number of rows and columns in the board
    numRows = len(board)
    numCols = len(board[0])

    # Forming the footer for the printed board: |R\C| a | b | c | d | e | f | g |
    footer = "|R\\C|"

    for col in ["a", "b", "c", "d", "e", "f", "g"]:
        footer += f" {col} |"

    # Forming the dashes that will be used as separations: -----------------
    dashes = ""

    for _ in range(len(footer)):
        dashes += "-"

    # Printing the board
    for row in range(numRows-1, -1, -1):
        line = f"| {row+1} |"

        for col in range(numCols):
            line += f" {board[row][col]} |"

        print(line)
        print(dashes)

    # Printing footer
    print(footer)
    print(dashes)

def createBoard():

    """ 
    Creates a board represented as a 2D array 
    
    Return:
        2D array (6x7) with empty spaces denoting empty entries
    """

    return [[" " for col in range(7)] for row in range(6)]

def insert(entry, symbol, board):
    
    """ 
    Accepts an entry in the form of column letter with row number (ex. c1)
    and inserts the symbol into the board at that spot
    """

    # Convert entry into integers for row and column
    rowNumber, colNumber = entryToCoords(entry)

    # Insert symbol into spot of the board
    board[rowNumber][colNumber] = symbol

def availablePositions(board):

    """ Finds valid spots where a player can insert their symbol """

    # Finding number of rows and columns
    numRows = len(board)
    numCols = len(board[0])

    # Find empty spot in each column (lowest row has priority)
    available = []

    for col in range(numCols):
        for row in range(numRows):
            if board[row][col] == " ":
                entry = coordsToEntry(row, col)
                available.append(entry)
                break

    return available


def cleanEntry(entry):

    """ Removes whitespaces froma user's input """
    return entry.replace(" ", "")

def entryToCoords(entry):

    """ Converts an entry in the form of column-letter with row number into (rowNum, colNum) """
    map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
    columnLetter = entry[0]
    rowNum = int(entry[1]) - 1
    colNum = map[columnLetter]
    return (rowNum, colNum)

def coordsToEntry(row, col):

    """ Converts (rowNum, colNum) to a string of the form column-letter with row number """
    map = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g"}
    columnLetter = map[col]
    return columnLetter + str(row+1)

def validateEntry(entry, availableSpots):

    """ 
    Verifies if entry follow column-letter with row number format
    and the user's input is in the list of available spots
    """

    # Check if entry is a column letter and row number
    if len(entry) != 2:
        return False
    
    columnLetter = entry[0]
    rowNumber = entry[1]

    if columnLetter not in ["a", "b", "c", "d", "e", "f", "g"]:
        return False
    if not str(rowNumber).isdigit():
        return False
    if int(rowNumber) < 1 or int(rowNumber) > 6:
        return False
    
    # Check if entry is in the list of available spots
    if entry not in availableSpots:
        return False

    return True

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

def checkWin(entry, board):

    """ 
    Checks if spot (entry) on board leads to a win

    For horizontal win, we count how many consecutive symbols are
    on the left and right of the spot in question. If the value
    is less than 4 then we know that spot did not lead to a win.
    Vertical and diagonal wins are checked similarly.
    """

    # Finding number of rows and columns in board
    numRows = len(board)
    numCols = len(board[0])

    # Converting entry to row and col number
    row, col = entryToCoords(entry)

    symbol = board[row][col]
    verticalWin = True
    horizontalWin = True
    leftDiagonalWin = True
    rightDiagonalWin = True
    
    # Check for a horizontal win
    numConsecutive = 1
    currentCol = col - 1
    while currentCol >= 0 and board[row][currentCol] == symbol:
        numConsecutive += 1
        currentCol -= 1
    
    currentCol = col + 1
    while currentCol < numCols and board[row][currentCol] == symbol:
        numConsecutive += 1
        currentCol += 1

    if numConsecutive < 4:
        horizontalWin = False

    # Check for a vertical win
    numConsecutive = 1
    currentRow = row - 1
    while currentRow >= 0 and board[currentRow][col] == symbol:
        numConsecutive += 1
        currentRow -= 1
    
    currentRow = row + 1
    while currentRow < numRows and board[currentRow][col] == symbol:
        numConsecutive += 1
        currentRow += 1

    if numConsecutive < 4:
        verticalWin = False

    # Check for a left diagonal win: \
    numConsecutive = 1
    currentRow = row - 1
    currentCol = col + 1
    while currentRow >= 0 and currentCol < numCols and board[currentRow][currentCol] == symbol:
        numConsecutive += 1
        currentRow -= 1
        currentCol += 1
    
    currentRow = row + 1
    currentCol = col - 1
    while currentRow < numRows and currentCol >= 0 and board[currentRow][currentCol] == symbol:
        numConsecutive += 1
        currentRow += 1
        currentCol -= 1

    if numConsecutive < 4:
        leftDiagonalWin = False

    # Check for a right diagonal win: /
    numConsecutive = 1
    currentRow = row + 1
    currentCol = col + 1
    while currentRow < numRows and currentCol < numCols and board[currentRow][currentCol] == symbol:
        numConsecutive += 1
        currentRow += 1
        currentCol += 1
    
    currentRow = row - 1
    currentCol = col - 1
    while currentRow >= 0 and currentCol >= 0 and board[currentRow][currentCol] == symbol:
        numConsecutive += 1
        currentRow -= 1
        currentCol -= 1

    if numConsecutive < 4:
        rightDiagonalWin = False

    # Return True if there is any type of win
    return True if (verticalWin or horizontalWin or leftDiagonalWin or rightDiagonalWin) else False

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

            # Get input from player to see what spot they want to place their symbol in
            while(entry is None):

                # Ask where to put player's symbol
                print(f"{symbols[turn]}'s turn.")
                print(f"Where do you want your {symbols[turn]} placed?")
                available = availablePositions(board)
                print(f"Available positions are: {available}")
                print()
                entry = input("Please enter column-letter and row-number (e.g., a1): ")
                entry = cleanEntry(entry)

                # If format was not followed or spot chosen is not available then ask them to try again
                if not validateEntry(entry, available):
                    print("Invalid entry: try again.")
                    print()
                    entry = None

            # Thank the player for a successful selection and update board
            print("Thank you for your selection.")
            insert(entry, symbols[turn], board)

            # Check if a player has won and ask if they want to go again
            if checkWin(entry, board):

                print()
                print(f"{symbols[turn]} IS THE WINNER!!!")
                printBoard(board)
                print()
                anotherGame = input("Another game (y/n)? ")
                print()

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
                anotherGame = input("Another game (y/n)? ")
                print()

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
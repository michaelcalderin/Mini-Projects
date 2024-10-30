"""
EGN5442 Mini-Project 2
Name: Michael Calderin
UFID: 84670557
Date: 10/31/2024

This program allows users to play Tic Tac Toe, built using classes and objects. The board 
is represented as a 2D array which is of 3x3 size. Player X starts and will be asked where 
to place their symbol. Input is validated to ensure it follows a format of row number 
followed by a comma and the column number. Extra spaces are acceptable but lack of integer 
inputs or numbers that are not within the range of the board will result in a request to try 
again. If the spot is already taken then the user will also be prompted to try again. The 
players will take turns making moves until a win (3 symbols are consecutively vertical,
horizontal, or diagonal) or a draw (full board). At this point, players will be asked if 
they want to go for another game.
"""

# Define Board class to building the Game Board:

class Board:

     # This constructor initiates the board with empty cells
    def __init__(self):
        self.c = [[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]]
      
    # This method prints the board. Recall that class methods are functions
    def printBoard(self):
        # It first prints the BOARD_HEADER constant
        # BOARD_HEADER constant
        BOARD_HEADER = "-----------------\n|R\\C| 0 | 1 | 2 |\n-----------------"
        print(BOARD_HEADER)

        # Using a for-loop, it increments through the rows
        for i in range(3):
            print(f"| {i} | {self.c[i][0]} | {self.c[i][1]} | {self.c[i][2]} |")
            print("-----------------")

    
# Define Game class to implement the Game Logic:

class Game:

    # The constructor
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    # This method switches players 
    def switchPlayer(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
    
    # This method validates the user's entry
    def validateEntry(self, row, col):

        """ Verifies if the user's input is a coordinate on the board """

        # Finding number of rows and columns in board
        numRows = len(self.board.c)
        numCols = len(self.board.c[0])

        # Return True if the spot is on the board, otherwise return False
        if 0 <= row < numRows and 0 <= col < numCols:
            return True
        
        return False

    # This method checks if the board is full
    def checkFull(self):

        """ Checks if the board is full by detecting empty spots """

        # Finding number of rows and columns in board
        numRows = len(self.board.c)
        numCols = len(self.board.c[0])

        # If empty spot is found then board is not full
        for row in range(numRows):
            for col in range(numCols):
                if self.board.c[row][col] == " ":
                    return False

        return True

    # This method checks for a winner
    def checkWin(self):
        
        """ Checks if (row, col) spot on board leads to a win """

        # Finding number of rows and columns in board
        numRows = len(self.board.c)
        numCols = len(self.board.c[0])
        verticalWin = False
        horizontalWin = False
        diagonalWin = False

        # Check for a vertical win
        for col in range(numCols):

            count = 0
            symbol = self.board.c[0][col]

            if symbol == " ":
                continue

            for row in range(numRows):

                if self.board.c[row][col] == symbol:
                    count += 1

            if count == 3:
                verticalWin = True
                break
        
        # Check for a horizontal win
        for row in range(numRows):

            count = 0
            symbol = self.board.c[row][0]

            if symbol == " ":
                continue

            for col in range(numCols):

                if self.board.c[row][col] == symbol:
                    count += 1

            if count == 3:
                horizontalWin = True
                break

        # Check for a diagonal win
        symbol = self.board.c[1][1]

        if symbol == " ":
            diagonalWin = False
        elif self.board.c[0][0] == symbol and self.board.c[1][1] == symbol and self.board.c[2][2] == symbol:
            diagonalWin = True
        elif self.board.c[2][0] == symbol and self.board.c[1][1] == symbol and self.board.c[0][2] == symbol:
            diagonalWin = True
        else:
            diagonalWin = False

        # Return True if there is any type of win
        return True if (verticalWin or horizontalWin or diagonalWin) else False

    # This method checks if the game has met an end condition by calling checkFull() and checkWin()
    # Hint: you can call a class method using self.method_name() within another class method, e.g., self.checkFull()
    def checkEnd(self):
        
        return self.checkFull() or self.checkWin()

    # This method runs the tic-tac-toe game
     # Hint: you can call a class method using self.method_name() within another class method
    def playGame(self):

        # Initial message and board for a new game
        print("New Game: X goes first.")
        print()
        self.board.printBoard()
        print()

        # Gane continues until an end scenario (win or full board)
        while (not self.checkEnd()):

            # Get User Input
            entry = None
            coord = None

            while (entry is None):

                # Ask where to put player's symbol
                print(f"{self.turn}'s turn.")
                print(f"Where do you want your {self.turn} placed?")
                print("Please enter row number and column number separated by a comma.")
                entry = input()

                # ----- Turning Entry Into Spot On Board -----

                # Split the input by comma to try to get [row, col]
                entry = entry.split(",")

                # If input cannot provide a pair for a coordinate then return None
                # Otherwise, try to convert user input into a row and column number
                if len(entry) != 2:
                    coord = None
                else:
                    row = -1
                    col = -1
                    try:
                        row = int(entry[0])
                        col = int(entry[1])
                        coord = (row, col)
                    except ValueError as e:
                        coord = None

                # ----------------------------

                # Tell player what they entered (will display "?" for row # and col # if format specified is not followed)
                if coord is None:
                    print(f"You have entered row #?")
                    print(f"{'':10}and column #?")
                else:
                    print(f"You have entered row #{coord[0]}")
                    print(f"{'':10}and column #{coord[1]}")

                # If format was not followed or the row/col # is not in the board then ask them to try again
                if (coord is None) or (not self.validateEntry(coord[0], coord[1])):
                    print("Invalid entry: try again.")
                    print("Row & column numbers must be either 0, 1, or 2.")
                    print()
                    entry = None
                # If cell they chose is already taken then ask them to try again
                elif (coord is not None) and (self.board.c[coord[0]][coord[1]] != " "):
                    print("That cell is already taken.")
                    print("Please make another selection.")
                    print()
                    entry = None

            # Thank the player for a successful selection and update board
            print("Thank you for your selection.")
            row, col = coord[0], coord[1]
            self.board.c[row][col] = self.turn

            # Check if a player has won
            if self.checkWin():
                print(f"{self.turn} IS THE WINNER!!!")
            # Check if the board is full (which is a tie)
            elif self.checkFull():
                print()
                print("DRAW! NOBODY WINS!")

            # Show the current board
            self.board.printBoard()
            print()

            # Change the turn to the next player
            self.switchPlayer()



# Main function
def main():
    # First initializes a variable to repeat the game
    repeat = True

    # Using while-loop that runs until the user says no for another game
    while (repeat):

        # Create game and play
        game = Game()
        game.playGame()

        # Ask user whether to do another game
        print("Another game? Enter Y or y for yes.")
        anotherGame = input()

        if anotherGame not in ["Y", "y"]:
            repeat = False

    # Goodbye message 
    print("Thank you for playing!")
    
# Call to main() function
if __name__ == "__main__":
    main()

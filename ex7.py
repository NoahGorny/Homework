"""

*Student Name: Noah Gorny

*Student ID: 209399757

*Course Exercise Group: 02 Math

*Exercise name: ex7

"""
import argparse  # mandatory
import random
import turtle
import string
import sys

def oldMysteryFunc(a, n):
    while a != 0:
        temp = a % n
        print temp
        a = a/n

def mysteryFunc(a, n):
    """
    Displays a with the base n witch recursion
    :param a: a must be a positive integer.
    He is the number in base 10 we will change his base.
    :param n: n must be a positive integer.
    He is the base we want to change a into.
    :return: Prints a as a number in base n
    """
    if(a>0):
        print a % n
        mysteryFunc(a/n, n)


class Sierpinski(object):

    def __init__(self):
        """
        Initialize Sierpinski with a new turtle and screen
        :param: No parmeters
        :return: None(alters self)
        """
        self.window = turtle.Screen()
        self.sierpinski_turtle = turtle.Turtle()

    def draw_sierpinski(self, length, depth):
        """
        draws a sierpinski tree
        :param length: the length of the base of the all tree
        :param depth: the depth of the tree recursion
        :return: None
        """
        # Draw the big triangle
        bob=self.sierpinski_turtle
        bob.left(60)
        bob.forward(length)
        bob.right(120)
        bob.forward(length)
        bob.right(120)
        bob.forward(length)
        bob.left(180)
        # Start to draw in recursion
        self.draw_recursion(length, depth)

    def draw_recursion(self, length, depth):
        if(depth>0):
            # Give a nice name for the turtle
            bob=self.sierpinski_turtle
            # Set the new length as length/2
            newLength=length/2
            # Draw a little triangle inside this triangle
            bob.left(60)
            bob.forward(newLength)
            bob.right(60)
            bob.forward(newLength)
            bob.right(120)
            bob.forward(newLength)
            bob.right(120)
            bob.forward(newLength)
            # Return to his base
            bob.left(120)
            bob.forward(newLength)
            bob.left(120)
            # Now do the same with the 3 mini triangles
            self.draw_recursion(newLength, depth-1)
            bob.left(60)
            bob.forward(newLength)
            bob.right(60)
            self.draw_recursion(newLength, depth-1)
            bob.right(60)
            bob.forward(newLength)
            bob.left(60)
            self.draw_recursion(newLength, depth-1)
            bob.left(180)
            bob.forward(newLength)
            bob.left(180)

    def finish_draw(self):
        """
        Closes the window in order to stop drawing
        :param: No parmeters
        :return: None(alters self)
        """
        self.window.bye()

    def save_draw(self, length, depth):
        """
        Saves the drawing in an svg file
        :param length: the length of the base of the all tree
        :param depth: the depth of the tree recursion
        :return: None(alters self)
        """
        self.sierpinski_turtle.hideturtle()
        nameSav = ("sierpinski_%d_%d" % (length, depth)) + ".svg"
        ts = turtle.getscreen().getcanvas()
        ts.postscript(file=nameSav).encode('utf-8')


class GameStatus(object):
    """Enum of possible Game statuses."""
    __init__ = None
    NotStarted, InProgress, Win, Lose = range(4)


class BoardCell(object):
    """
    Represents a cell in the minesweeper board game and is current status in the game

    """
    def __init__(self):
        """
        Initializes a board cell with no neighboring mines and status is hidden

        Args:
            None

        Returns:
            None (alters self)
        """
        self.hidden=True
        self.mine=False
        self.neighbor_mines=0

    def is_mine(self):
        """
        returns true if this cell contains a mine false otherwise

        Args:
            None

        Returns:
            true if this cell contains a mine false otherwise
        """
        return self.mine

    def is_hidden(self):
        """
        returns true if this cell is hidden false otherwise

        Args:
            None

        Returns:
            true if this cell is hidden false otherwise
        """
        return self.hidden

    def get_cell_value(self):
        """
        returns the number of adjacent mines

        Args:
            None

        Returns:
            the number of adjacent mines in int or the charcter '*' if this cell is a mine
        """
        return self.neighbor_mines

    def uncover_cell(self):
        """
        uncovers this cell. when a cell is uncovered then is status is the value of the mines near it or * if the
        cell is a mine
        Args:
            None

        Returns:
            None (alters self)

        """
        self.hidden=False

    def update_cell_value(self, cellValue):
        """
        updates the value of the how many neighboring mines this cell has

        Args:
            numOfNearMine - the new number of the how many neighboring mines this cell has

        Returns:
            None (alters self)
        """
        self.neighbor_mines=cellValue

    def add_one_to_cell_value(self):
        """
        adds one to the number of near mine

        Args:
            None

        Returns:
            None (alters self)
        """
        if(not self.mine):
            self.neighbor_mines+=1

    def set_has_mine(self):
        """
        changes this cell to a cell with a mine in it

        Args:
           None

        Returns:
            None (alters self)
        """
        self.mine=True
        self.neighbor_mines='*'


class Board(object):
    """Represents a board of minesweeper game and its current progress."""

    def __init__(self, rows, columns):
        """Initializes an empty hidden board.

        The board will be in the specified dimensions, without mines in it,
        and all of its cells are in hidden state.

        Args:
            rows: the number of rows in the board
            columns: the number of columns in the board

        Returns:
            None (alters self)
        """
        self.numRows = rows
        self.numColumns = columns
        # starts a board with row*col board cells
        self.board = [[BoardCell() for _ in range(columns)] for _ in range(rows)]

    def put_mines(self, mines, seed=None):
        """Randomly scatter the requested number of mines on the board.

        At the beggining, all cells on the board are hidden and with no mines
        at any of them. This method scatters the requested number of mines
        throughout the board randomly, only if the board is in the beginning
        state (as described here). A cell can host only one mine.
        This method not only scatters the mines on the board, but also updates
        the cells around it (so they will hold the right digit).

        Args:
            mines: the number of mines to scatter
            seed: the seed to give the random function. Default value None

        Returns:
            None (alters self)

        """
        listOfCellsIndex = [(numRow, numCol) for numRow in range(self.numRows) for numCol in range(self.numColumns)]
        # randomly choosing cells in the board to place mines in
        random.seed(seed)
        listOfMineCells = random.sample(listOfCellsIndex, mines)
        for (row, col) in listOfMineCells:
            # Update the cell
            self.board[row][col].set_has_mine()
            # Update the nearby cells
            self.update_nearby_cells(row, col)


    def update_nearby_cells(self, row, col):
        """
        Updates the adjecent cells of the cell board[row][col] by
        increasing their mine counter by one.

        Args:
            row: the row of the new mine
            col: the column of the new mine

        Returns:
            None (alters self)
        """
        for (i, j) in [(x,y) for x in [-1,0,1] for y in[-1,0,1]]:
            # Check if the indicies are still in range
            if ((row+i<self.numRows) and (col+j<self.numColumns)
            and (row+i>=0) and (col+j>=0)):
                if(not self.board[row+i][col+j].is_mine()):
                    # This nearby cell is not a mine, add 1 to his value
                    self.board[row+i][col+j].add_one_to_cell_value()


    def print_board(self):
        """prints the board according to the game format
            DO NOT CHANGE ANYTHING IN THIS FUNCTION!!!!!!!
        Args:
            None
        Returns:
            None
        """
        # creates the printing format
        printFormatString = "%-2s " * self.numColumns
        printFormatString += "%-2s"
        # prints the first line of the board which is the line containing the indexes of the columns
        argList = [" "]
        argList.extend([str(i) for i in range(self.numColumns)])
        print printFormatString % tuple(argList)
        # goes over the board rows and prints each one
        for i in range(self.numRows):
            argList = [str(i)]
            for j in range(self.numColumns):
                if self.board[i][j].is_hidden():
                    argList.append("H")
                else:
                    argList.append(str(self.board[i][j].get_cell_value()))
            print printFormatString % tuple(argList)

    def load_board(self, lines):
        """Loads a board from a sequence of lines.

        This method is used to load a saved board from a sequence of strings
        (that usually represent lines). Each line represents a row in the table
        in the following format:
            XY XY XY ... XY
        Where X is one of the characters: 0-8, * and Y is one of letters: H, S.
        0-8 = number of adjusting mines (0 is an empty, mine-free cell)
        * = represents a mine in this cell
        H = this cell is hidden

        The lines can have multiple whitespace of any kind before and after the
        lines of cells, but between each XY pair there is exactly one space.
        Empty or whitespace-only lines are possible between valid lines, or after/before them.
        It is safe to assume that the values are correct (the number represents the number of mines around
        a given cell) and the number of mines is also legal.

        Note that this method doesn't get the first two rows of the file (the
        dimensions) on purpose - they are handled in __init__.

        Args:
            lines: a sequence (list or tuple) of lines with the above restrictions

        Returns:
            None (alters self)
        """
        numMines=0
        # Get amount of rows and columns
        (row, column)=(int(lines[0]), int(lines[1]))
        for i in range(0, len(lines)-2):
            # Get the current line splitted
            line=lines[i+2].split()
            for j in range(0, len(line)):
                # Get the current cell
                cell=line[j]
                if(cell[1]!='H'):
                    # Uncover the cell
                    self.board[i][j].uncover_cell()
                if(cell[0]=='*'):
                    # Increase the number of mines
                    numMines+=1
                    self.board[i][j].set_has_mine()
                else:
                    # Just set the cell value to his size in the text
                    self.board[i][j].update_cell_value(int(cell[0]))
        if(numMines>row*column-1):
            # Bad amount of mines
            print "Illegal board"
            exit(0)

    def get_value(self, row, column):
        """Returns the value of the cell at the given indices.

        The return value is a string of one character, out of 0-8 + '*'.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            If the cell is empty and has no mines around it, return '0'.
            If it has X mines around it (and none in it), return 'X' (digit
            character between 1-8).
            If it has a mine in it return '*'.

        """
        return self.board[row][column].get_cell_value()

    def is_hidden(self, row, column):
        """Returns if the given cell is in hidden or uncovered state.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            'H' if the cell is hidden, or 'S' if it's uncovered (can be seen).
        """
        if(self.board[row][column].is_hidden()):
            return 'H'
        # Return S otherwise
        return 'S'

    def uncover(self, row, column):
        """Changes the status of a cell from hidden to seen.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            None (alters self)
        """
        self.board[row][column].uncover_cell()


class Game(object):
    """Handles a game of minesweeper by supplying UI to Board object."""

    def __init__(self, board):
        """Initializes a Game object with the given Board object.

        The Board object can be a board in any given status or stage.

        Args:
            board: a Board object to continue (or start) playing.

        Returns:
            None (alters self)
        """
        self.theBoard=board
        # Just to intialize
        self.status=GameStatus.NotStarted

    def get_status(self):
        """Returns the current status of the game.

        The current status of the game is as followed:
            NotStarted: if all cells are hidden.
            InProgress: if some cells are hidden and some are uncovered, and
            no cell with a mine is uncovered.
            Lose: a cell with mine is uncovered.
            Win: All non-mine cells are uncovered, and all mine cells are
            covered.

        Returns:
            one of GameStatus values (doesn't alters self)

        """
        return self.status

    def make_move(self, row, column):
        """Makes a move by uncovering the given cell and unrippling it's area.

        The move flow is as following:
        1. Uncover the cell
        2. If the cell is a mine - return
        3. if the cell is not a mine, ripple (if value = 0) and uncover all
            adjacent cells, and recursively on this cells if needed (if they are empty cells)

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            the cell's value.
        """
        # Uncover the cell
        self.theBoard.uncover(row, column)
        # Get the current cell
        currentCell=self.theBoard.board[row][column]
        if(not currentCell.is_mine()):
            # The cell is not a mine
            if(currentCell.get_cell_value()==0):
                # The cell has 0 value, ripple it
                self.ripple(row, column)
        # Return the cell's value
        return currentCell.get_cell_value()

    def ripple(self, row, col):
        """
        Reveal all the adjecent cells of the cell board[row][col].
        Reveals them by calling make_move on them IF THEY ARE NOT REVEALED YET

        Args:
            row: row index of the rippled cell (integer)
            column: column index of the rippled cell (integer)

        Returns:
            None (alters self)
        """
        for (i, j) in [(x,y) for x in [-1,0,1] for y in[-1,0,1]]:
            # Check if the indicies are still in range
            if ((row+i<self.theBoard.numRows) and (col+j<self.theBoard.numColumns) 
            and (row+i>=0) and (col+j>=0)):
                # Checks if the nearby cell is already revealed
                if(self.theBoard.board[row+i][col+j].is_hidden()):
                    # Reveal the nearby cell
                    self.make_move(row+i, col+j)


    def update_status(self):
        """
        Updates the status of the game.
        First it sets the status to NotStarted.
        Checks if there is a revealed mine, if there is it's Lose.
        If there is a revealed cell which is not a mine it changes
        the status to InProgress for the time being.
        If it finds an hidden cell who is not a mine it knows
        we didnt won. If it reached the end and no such cell
        was found, it changes the status to Win.

        Args:
            None

        Returns:
            None (alters self)
        """
        # Boolean to know if we have won
        won=True
        # Set the status to NotPlayed at the start
        self.status=GameStatus.NotStarted
        for lineOfCells in self.theBoard.board:
            for cell in lineOfCells:
                if(not cell.is_hidden()):
                    # The cell is revealed
                    if(cell.is_mine()):
                        # Mine revealed, we lost
                        self.status=GameStatus.Lose
                        return
                    else:
                        # We have a revealed cell, its in progress
                        self.status=GameStatus.InProgress
                else:
                    if(not cell.is_mine()):
                        # We have a good cell that is still hidden
                        won=False
        # Check if we had won
        if(won):
            self.status=GameStatus.Win


    def run(self):
        """Runs the game loop.

        At each turn, prints the following:
            current state of the board
            game status
            available actions
        And then wait for input and act accordingly.
        More details are in the project's description.

        Returns:
            None
        """
        # Update the status at the start
        self.update_status()
        # To recieve the user input
        playerInput=0
        while (playerInput!=1):
            # To know if there were bad inputs
            badMove=False
            badChoice=False
            self.print_menu()
            # Get the first player input
            playerInput=raw_input("Enter selection:\n")
            # Check if the input is ok
            if(playerInput.isdigit()):
                playerInput=int(playerInput)
            else:
                # Bad format
                badChoice=True
            if(playerInput==1):
                # Exit the game
                print "Goodbye :)"
            elif(playerInput==2):
                # Check if we have won already
                if((self.status==GameStatus.Win) or (self.status==GameStatus.Lose)):
                    # Cant choose 2 when the game is finished
                    badChoice=True
                else:
                    # Make a move
                    self.move_turn()
            else:
                # Bad choice, not 1 or 2
                badChoice=True
            if(badChoice):
                print "Illegal choice"

    def move_turn(self):
        """
        Do a move turn by asking for a position input and trying to make a move
        in this place (after checking for legal input)
        It gets the input, checks to see if its ok and then calls make_move
        and update_status.


        Args:
            None

        Returns:
            None (alters self)
        """
        # Get row and column
        badMove=False
        playerInput=raw_input("Enter row then column (space separated): \n")
        if(len(playerInput)!=3):
            # Not in the currect format
            badMove=True
        else:
            # Make them ints
            (row,column)=(int(playerInput[0]), int(playerInput[2]))
            if((row>=0) and (column>=0) and (row<self.theBoard.numRows) 
            and (column<self.theBoard.numColumns)):
                # Rows and col are in border
                if(self.theBoard.is_hidden(row, column)=='H'):
                    # The cell is hiddem, make a move
                    self.make_move(row, column)
                    # Update the status
                    self.update_status()
                else:
                    # Already revealed
                    badMove=True
            else:
                # Out of border
                badMove=True
        if(badMove):
            print "Illegal move values"

    def print_menu(self):
        """
        Prints the whole menu.
        Print the board using print_board and then prints the status
        and the available options.

        Args:
            None

        Returns:
            None
        """
        # Print the board
        self.theBoard.print_board()
        # Print the status
        if(self.status==GameStatus.NotStarted):
            msg="NotStarted"
        elif(self.status==GameStatus.InProgress):
            msg="InProgress"
        elif(self.status==GameStatus.Win):
            msg="Win"
        elif(self.status==GameStatus.Lose):
            msg="Lose"
        print "Game status: "+msg
        # Print the options
        available= "Available actions: (1) Exit"
        if(self.status==GameStatus.NotStarted or self.status==GameStatus.InProgress):
            available+=(" | (2) Move")
        print available


def main():
    """Starts the game by parsing the arguments and initializing.
    Act according to the exercise explanation

    Regarding mine swiper:
    If an input file argument was given, the file is loaded (even if other
    legal command line argument were given).

    If input file wasn't given, create a board with the rows/columns/mines

    In case both an input file was given and other parameters, ignore the
    others and use only the input file.
    For example, in case we get "-i sample -r 2 -c 2" just use
    the input file and ignore the rest (even if there are missing parameters).

    Returns:
        None

    """
    # To allow bigger recursion
    sys.setrecursionlimit(2100)
    # The main parser
    mainParser=argparse.ArgumentParser();
    mainParser.add_argument('-p', type=int, required=True);
    # Mission 1 arguments
    mainParser.add_argument('-a', type=int);
    mainParser.add_argument('-n', type=int);
    # Mission 2 arguments
    mainParser.add_argument('-l', type=int);
    mainParser.add_argument('-d', type=int);
    # Mission 3 arguments
    mainParser.add_argument('-r', type=int);
    mainParser.add_argument('-c', type=int);
    mainParser.add_argument('-i', type=argparse.FileType('r+'), default=None);
    mainParser.add_argument('-m', type=int);
    mainParser.add_argument('-s', type=float, default=None);
    # Parse the arguments
    args=mainParser.parse_args();
    # Proccess them
    proccess(args)

def proccess(parsed):
    """
    Process the input, choose depends on parsed.p which mission to choose.
    Then calls the appropriate functions.

    Args:
        parsed: The arguments (mainParser.parse_args() type)

    Returns:
        None
    """
    mainChoice=parsed.p
    if(mainChoice==1):
        # Call the mystery func
        mysteryFunc(parsed.a, parsed.n)
    elif(mainChoice==2):
        # Create a new Sierpinski
        sierpinski=Sierpinski()
        # draw it
        sierpinski.draw_sierpinski(parsed.l, parsed.d)
        # save the drawing
        sierpinski.save_draw(parsed.l, parsed.d)
        # Close the draw
        sierpinski.finish_draw()
    elif(mainChoice==3):
        # Call the mine sweeper proccessor
        processMineSweeper(parsed)

def processMineSweeper(parsed):
    """
    Process the input, checks if we got a file in our input, if we did
    it cleans the file from unwanted newlines and blank line and initializes
    the board using the first two lines. Afterwards it calls load_board
    to set up the board. If no input was found it gets row and column from the
    arguments and initializes the board. Afterwards it calls put_mines to put
    new mines in the empty board.
    At the end it creates a game using the board and call the run() function

    Args:
        parsed: The arguments for the minesweeper.

    Returns:
        None
    """
    if (parsed.i is not None):
        with parsed.i as boardFile:
            # Sort the lines
            lines=[line.strip() for line in boardFile if line.strip()]
            # Get the rows and the columns
            (rows, columns)=(int(lines[0]), int(lines[1]))
            if((rows>=1 and rows<=20) and (columns>=2 and columns<=50)):
                # Create board with rows and col
                board=Board(rows, columns)
                # Load the board
                board.load_board(lines)
            else:
                print "Illegal board"
                exit(0)
    else:
        # Get the rows and the columns
        rows=parsed.r
        columns=parsed.c
        if((rows>=1 and rows<=20) and (columns>=2 and columns<=50) 
        and (parsed.m<=(rows*columns-1))):
            # Create the board with rows and col
            board=Board(rows, columns)
            # Put the mines
            if(parsed.s is not None):
                board.put_mines(parsed.m, parsed.s)
            else:
                board.put_mines(parsed.m)
        else:
            # Bad board, exit
            print "Illegal board"
            exit(0)
    # Create a new game object
    theGame=Game(board)
    # Play the game
    theGame.run()

if __name__ == '__main__':
    main()

# ADD NO CODE OUTSIDE MAIN() OR OUTSIDE A FUNCTION/CLASS (NO GLOBALS), EXCEPT IMPORTS WHICH ARE FINE

# student name: Peter Kim
# student number: 18693002

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list 
    """
    print() # Line break

    row_separator = "--+---+--"

    # Loop through the starting indices of each row in a 3x3 grid
    for i in range(0, 9, 3):
        # Print the current row of the board and its indices
        print(f"   {board[i]} | {board[i+1]} | {board[i+2]}    {i} | {i+1} | {i+2}")
        
        # Print a row separator if this is not the last row
        if i < 6:
            print(f"   {row_separator}    {row_separator}")

    print() # Line break

def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    while True:
        try:
            # Ask the player for a cell number
            user = int(input("Next move for X (state a valid cell num): "))

            # Check if the cell number is valid and not already occupied
            if user < 0 or user > 8 or board[user] != ' ':
                print("Must enter a valid cell number")
            else:
                # Update the board with the player's move
                print("You chose cell", user)
                board[user] = 'X'
                played.add(user)
                break
        except ValueError:
            # Handle non-integer inputs
            print("Must be an integer")

    printBoard()  # Show the updated board

def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    while True:
        # Pick a random cell number between 0 and 8
        ai = random.randint(0, 8)

        # If the cell is taken, choose another one
        if board[ai] != ' ':
            continue
        else:
            # If the cell is free, make the move
            print("Computer chose cell", ai)
            board[ai] = 'O'
            played.add(ai)
            break

    printBoard()  # Show the updated board

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """

    who_pos = set()  # Initialize an empty set to hold positions for 'who'

    win_comb = [
        {0, 1, 2},  # Top row
        {3, 4, 5},  # Middle row
        {6, 7, 8},  # Bottom row
        {0, 3, 6},  # Left column
        {1, 4, 7},  # Middle column
        {2, 5, 8},  # Right column
        {0, 4, 8},  # Diagonal from top-left to bottom-right
        {2, 4, 6}   # Diagonal from top-right to bottom-left
    ]

    for pos in played:  # Iterate over each position in the global played set
        if board[pos] == who:   # Check if the board position is occupied by 'who'
            who_pos.add(pos)    # Add the position to the who_pos set

    for combo in win_comb:  # Check if any winning combination is a subset of who_pos
        if combo.issubset(who_pos):
            return True  # 'who' has won

    return False

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """

    who_pos = set()  # Initialize an empty set to hold positions for 'who'

    win_comb = [
        {0, 1, 2},  # Top row
        {3, 4, 5},  # Middle row
        {6, 7, 8},  # Bottom row
        {0, 3, 6},  # Left column
        {1, 4, 7},  # Middle column
        {2, 5, 8},  # Right column
        {0, 4, 8},  # Diagonal from top-left to bottom-right
        {2, 4, 6}   # Diagonal from top-right to bottom-left
    ]

    for pos in played:  # Iterate over each position in the global played set
        if board[pos] == who:   # Check if the board position is occupied by 'who'
            who_pos.add(pos)    # Add the position to the who_pos set

    for combo in win_comb:  # Check if any winning combination is a subset of who_pos
        if combo.issubset(who_pos):
            print("You won! Thanks for playing." if who == 'X' else "You lost! Thanks for playing.")
            return True  # 'who' has won

    # Check for a draw or a blocked game
    if len(played) == 9:
        print("A draw! Thanks for playing.")
        return True

    return False

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate
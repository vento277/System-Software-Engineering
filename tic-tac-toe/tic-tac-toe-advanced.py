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
        def get_safe_corners() -> list:
            safe_corners = []

            # Add corners based on the absence of 'X' in specific positions
            if board[1] != 'X':
                safe_corners.extend([0, 2])
            if board[3] != 'X':
                safe_corners.extend([0, 6])
            if board[5] != 'X':
                safe_corners.extend([2, 8])
            if board[7] != 'X':
                safe_corners.extend([6, 8])

            # Convert list to a set to remove duplicates and keep only empty corners
            safe_corners = list(set(corner for corner in safe_corners if board[corner] == ' '))

            # Remove corners based on specific dangerous patterns
            dangerous_patterns = {
                6: (8, 7),  # If 'O' is at 8 and 'X' is at 7, remove corner 6
                0: (2, 1),  # If 'O' is at 2 and 'X' is at 1, remove corner 0
                2: (0, 1),  # If 'O' is at 0 and 'X' is at 1, remove corner 2
                8: (6, 7)   # If 'O' is at 6 and 'X' is at 7, remove corner 8
            }

            # Remove unsafe corners based on the dangerous patterns
            for corner, (o_pos, x_pos) in dangerous_patterns.items():
                if corner in safe_corners and board[o_pos] == 'O' and board[x_pos] == 'X':
                    safe_corners.remove(corner)

            return safe_corners     

        def get_opposing_corner() -> int:
            # Define opposing corner pairs
            opposing_corners = {
                0: 8,
                2: 6,
                6: 2,
                8: 0
            }

            # Look for O in any of the corners and return the opposing corner
            for corner, opposite in opposing_corners.items():
                if board[corner] == 'O':
                    return opposite

            # If no O is found in corners or X is not at 4, return None or some indication
            return None

        def get_empty_sides() -> None:
            return [i for i in [1, 3, 5, 7] if board[i] == ' ']
        
        def find_missing_elements(combinations, elements):
            # Convert the provided elements to a set
            elements_set = set(elements)

            # Track missing elements
            missing_elements = set()

            # Check each combination
            for combo in combinations:
                # Count how many provided elements are in the current combination
                common_elements = elements_set.intersection(combo)

                # If at least two of the provided elements are present in the combination
                if len(common_elements) >= 2:
                    # Determine which elements from the combination are not in the provided elements
                    missing_elements.update(combo - elements_set)
                else:
                    pass

            return missing_elements

        win_comb = [
                {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # Rows
                {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # Columns
                {0, 4, 8}, {2, 4, 6}  # Diagonals
            ]

        X_pos = set()
        O_pos = set()
        for pos in played:  # Iterate over each position in the global played set
            if board[pos] == 'X':   # Check if the board position is occupied by 'X'
                X_pos.add(pos)    # Add the position to the X_pos set
        for pos in played:  # Iterate over each position in the global played set
            if board[pos] == 'O':   # Check if the board position is occupied by 'X'
                O_pos.add(pos)    # Add the position to the X_pos set

        block = find_missing_elements(win_comb, X_pos)
        attack = find_missing_elements(win_comb, O_pos)

        # When 'O' plays first
        if len(played) == 0:
            user = random.choice([0, 2, 6, 8])
        
        # If X places 'X' at the cente after first move, target the opposing corner.
        elif len(played) == 2 and board[4] == 'X':
            user = get_opposing_corner()
        
        # If X places 'X' anywhere else, target the adjecent corners.
        else:
            if bool(attack) and board[sorted(attack)[0]] == ' ':
                user = sorted(attack)[0]
            elif bool(block) and board[sorted(block)[0]] == ' ':
                user = sorted(block)[0]
            else:
                safe_corners = get_safe_corners()
                if safe_corners:
                    user = random.choice(safe_corners)
                else:
                    empty_sides = get_empty_sides()
                    if empty_sides:
                        user = random.choice(empty_sides)
                    else:
                        user = random.choice([i for i in range(9) if board[i] == ' '])

        print("Computer chose cell", user)
        board[user] = 'O'
        played.add(user)
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
    init()
    # if random.randrange(2) == 1:        # Random draw (50-50) to decide whether the gamer starts first or the computer starts first.
    #     print("Player X starts first")
    # while True:
    #     playerNextMove()            # X starts first
    #     if(terminate('X')): break   # if X won or a draw, print message and terminate
    #     computerNextMove()          # computer plays O
    #     if(terminate('O')): break   # if O won or a draw, print message and terminate
    # else:
    #   print("Player O starts first")
    while True:
        computerNextMove()          # O starts first
        if(terminate('O')): break   # if O won or a draw, print message and terminate
        playerNextMove()            # user plays X
        if(terminate('X')): break   # if X won or a draw, print message and terminate




        # #if center, first corner and block
        # elif len(played) == 1 and board[4] == 'X':
        #     user = random.choice(get_safe_corners())

        # else:
        #     if bool(attack) and board[sorted(attack)[0]] == ' ':
        #         user = sorted(attack)[0]
        #     elif bool(block) and board[sorted(block)[0]] == ' ':
        #         user = sorted(block)[0]
        #     else:
        #         safe_corners = get_safe_corners()
        #         if safe_corners:
        #             user = random.choice(safe_corners)
        #         else:
        #             empty_sides = get_empty_sides()
        #             if empty_sides:
        #                 user = random.choice(empty_sides)
        #             else:
        #                 user = random.choice([i for i in range(9) if board[i] == ' '])
        
        #         # When 'X' plays first and choses corner for an edge, target the center
        # if len(played) == 1 and board[4] != 'X':
        #     ai = 4
            
        # # Continue playing the edge unless there is a need to block
        # elif len(played) > 1 and board[4] != 'X':
        #     if bool(attack) and board[sorted(attack)[0]] == ' ':
        #         ai = sorted(attack)[0]
        #     elif bool(block) and board[sorted(block)[0]] == ' ':
        #         ai = sorted(block)[0]
        #     else:
        #         while True:
        #             ai = random.choice([1, 3, 5, 7])
        #             if board[(ai)] == ' ':
        #                 break
        #             else:
        #                 ai = random.choice([1, 3, 5, 7])
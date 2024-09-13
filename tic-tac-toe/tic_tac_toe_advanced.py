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
    """ computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    while True:
        def get_safe_corners() -> list:
            """ Determine the corners that are optimal for the player to occupy
                based on the current state of the board and the positions of 'X' and 'O'.
            """
            safe_corners = []

            # Check each corner and add it to the list if it is not occupied by 'X'
            if board[1] != 'X': safe_corners.extend([0, 2])
            if board[3] != 'X': safe_corners.extend([0, 6])
            if board[5] != 'X': safe_corners.extend([2, 8])
            if board[7] != 'X': safe_corners.extend([6, 8])

            # Remove duplicate corners and retain only those that are empty
            safe_corners = list(set(corner for corner in safe_corners if board[corner] == ' '))

            # Define patterns where placing 'O' in a specific corner and 'X' in another would make certain corners unsafe due to potential winning combinations for 'X'
            # (position of 'O', position of 'X'): [list of unsafe corners]
            dangerous_patterns = { 
                (0, 1): [2, 8], (0, 3): [6, 8], (0, 7): [8], (0, 5): [8],   
                (8, 7): [0, 6], (8, 5): [0, 2], (8, 1): [0], (8, 3): [0],  
                (2, 1): [0, 6], (2, 5): [6, 8], 
                (6, 7): [8, 2], (6, 3): [0, 2]    
            } 
            # The reason 2 and 6 dose not consider corners like 0 and 8 is beacuse the cell select algorithm below removes them by selecting the largest of all avilable corners.
            # For example, (2, 7), the ideal is 0 or 8 - 8 will be chosen. For (6, 1), the ideal is 0 or 8 - 8 will be chosen.

            # Iterate over each dangerous pattern to check if any unsafe corners should be removed
            for (o_pos, x_pos), unsafe_corners in dangerous_patterns.items():
                if board[o_pos] == 'O' and board[x_pos] == 'X': # Check if the current board configuration matches the dangerous pattern i.e., if 'O' is in the position o_pos and 'X' is in the position x_pos
                    safe_corners = [corner for corner in safe_corners if corner not in unsafe_corners] # If the pattern is matched, remove corners listed in unsafe_corners from the list of safe corners

            return safe_corners  

        def get_opposing_corner() -> int:
            """ Checks the corners to find out if there is an 'O' present in any of them. If found,
                it returns the corner that is directly opposite to it. This is useful when 'X' is placed at the center cell
                on the 2nd move - as the ideal strategy is to choose the opposing cell, making 'OXO' diagonally
            """
            # Define a mapping of corners to their opposing corners
            # position of 'O': corners directly opposite
            opposing_corners = {0: 8, 2: 6, 6: 2, 8: 0}

            # Iterate through each corner and its corresponding opposite corner
            for corner, opposite in opposing_corners.items():
                if board[corner] == 'O':
                    return opposite
                
            return None
                
        def find_missing_elements(combinations, elements) -> set:
            """ Evaluate each combination to determine which elements are present in the combination but not in the 
                provided set of elements. It is useful for finding single gaps in cells which are either to be blocked or attacked.
            """
            missing_elements = set()

            for combo in combinations:
                common_elements = elements.intersection(combo) # Find the intersection of the current combination with the set of provided elements

                # If at least two elements from the provided set are present in the combination, identify the element and update the set
                if len(common_elements) >= 2:
                    missing_elements.update(combo - elements)

            return missing_elements
        
        def find_winning_moves(win_comb, o_moves, all_moves) -> set:
            """ Analyzes each combination of cells that may lead to a win. It checks if exactly one 'O' is present
                in the combination and if the combination contains exactly two empty cells. If both conditions are met, the function 
                considers the empty cells as potential winning moves for 'O' but not necessarily the final one. 
            """
            potential_moves = set()
            all_cells = set(range(9))

            # Determine the set of empty cells by subtracting the occupied cells from the full set
            empty_cells = all_cells - set(all_moves)
            
            for combo in win_comb:
                # Find the intersection of the current combination with the cells occupied by 'O'
                o_in_combo = combo.intersection(o_moves)

                # Find the intersection of the current combination with the empty cells
                empty_in_combo = combo.intersection(empty_cells)
                
                # If exactly one 'O' is in the combination and exactly two cells are empty, add the empty cells to the set of potential winning moves
                if len(o_in_combo) == 1 and len(empty_in_combo) == 2:
                    potential_moves.update(empty_in_combo)

            return potential_moves
        
        def find_threes(X_pos) -> set:
            """ Determines which corners to be blocked for making a two-way win condition based on the current positions of 'X'. 
                It does so by checking for specific pairs of positions occupied by 'X' and mapping them to corresponding safe corners. 
            """
            found_corners = set()

            # Define a mapping of specific pairs of positions to their corresponding safe corner
            pattern = {
                (1, 3): 0, (3, 1): 0,  # Pair (1, 3) or (3, 1) maps to corner 0...so on
                (1, 5): 2, (5, 1): 2,  
                (3, 7): 6, (7, 3): 6,  
                (5, 7): 8, (7, 5): 8   
            }   
            
            # Convert the tuple of positions to a sorted list of unique positions
            unique_positions = sorted(X_pos)          
            
            # Check all pairs of positions from unique_positions
            for i in range(len(unique_positions)):
                for j in range(i + 1, len(unique_positions)):
                    pair = (unique_positions[i], unique_positions[j])

                    # Check if this pair matches any pattern
                    corner = pattern.get(pair)
                    if corner != None: found_corners.add(corner)
        
            return found_corners

        ai = None

        # Define all possible winning combinations on the board
        win_comb = [
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # Horizontal rows
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # Vertical columns
            {0, 4, 8}, {2, 4, 6}  # Diagonals
        ]

        # Identify positions occupied by 'X' and 'O' from the set of played positions
        X_pos = {pos for pos in played if board[pos] == 'X'}
        O_pos = {pos for pos in played if board[pos] == 'O'}

        # Determine moves needed to block 'X' from winning or to complete a winning combination for 'O'
        block = find_missing_elements(win_comb, X_pos)  # Moves to block 'X'
        finish = find_missing_elements(win_comb, O_pos)  # Moves to complete 'O'

        # Determine moves that have the potencial of making a winning combination for 'O'
        attack = find_winning_moves(win_comb, O_pos, played)

        # Find corners that are ideally played under certain circumstances
        safe_corners = get_safe_corners()

        # Identify potential moves that can create a two-way win situation for 'X'
        two_way = find_threes(X_pos)

        # -----Decision-making process for the Computer's move-----
        # If the Computer Starts:

        # 1. Take the Corner:
        #    - If the User Responds with the Center:
        #      - Take the diagonally opposite corner.
        #      - Continue defending to force a draw or capitalize on any mistakes to win.
        #    - If the User Responds with Anything Other Than the Center:
        #      - This leads to a guaranteed win. Take the corner that is not diagonal but has the user’s cell in between to force them to block the space in between.
        #      - Take the center, setting up a two-way winning scenario.

        # If the User Starts:

        # 1. If the User Starts with the Center:
        #    - Take any corner.
        #    - Continue defending to force a draw or win if the user makes a mistake.

        # 2. If the User Starts with a Non-Center Move:
        #    - Take the center.
        #    - Continue defending to force a draw or win if the user makes a mistake.

        # 3. Blocking a Two-Way Winning Scenario:
        #    - If the user plays two edge moves and takes a corner on their third move, this could create a two-way winning possibility. This must be blocked.

        # ---When 'O' plays first---

        # Play any of the four corners
        if len(played) == 0:
            ai = random.choice([0, 2, 6, 8])  

        # If 'X' has played the center, choose an opposing corner on the second move
        elif len(played) == 2 and board[4] == 'X':
            ai = get_opposing_corner()

        # If 'X' has not played the center by the fourth move, play the center
        elif len(played) == 4 and board[4] != 'X':
            ai = 4

        # If the center is occupied or if the game is in other specific states, prioritize moves from
        # 1. Finishing the game
        # 2. Blocking the opponents finishing move
        # 3. Playing the optimal corners
        # 4. Playing any possible cells with one 'O' and two empty spaces.
        # 5. Playing any left-over cells
        elif (len(played) == 2 and board[4] != 'X') or (len(played) == 4 and board[4] == 'X') or len(played) in {6, 8}:
            for moves in [finish, block, safe_corners, attack]:
                if ai == None:
                    for i in sorted(moves):
                        if board[i] == ' ':
                            ai = i
                            break

            if ai == None: ai = random.choice([i for i in range(9) if board[i] == ' '])  # Random move if no other move is available

        # ---When 'X' plays first---
        # If 'X' plays the center, play any one of the four corners
        elif len(played) == 1 and board[4] == 'X':
            ai = random.choice(get_safe_corners())

        # If 'X' plays a corner or edge, play the center
        elif len(played) == 1 and board[4] != 'X':
            ai = 4

        # If the game is in other specific states, prioritize moves from
        # 1. Finishing the game
        # 2. Blocking the opponents finishing move
        # 3. Blocking any possible two-ways to be formed
        # 4. Playing any possible cells with one 'O' and two empty spaces.
        # 5. Playing any left-over cells
        else:
            for moves in [finish, block, two_way, attack]:
                if ai == None:
                    for i in sorted(moves):
                        if board[i] == ' ':
                            ai = i
                            break

            if ai == None: ai = random.choice([i for i in range(9) if board[i] == ' '])  # Random move if no other move is available

        print("Computer chose cell", ai) 
        board[ai] = 'O' 
        played.add(ai) 
        break

    printBoard()

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise 
    """
    who_pos = set()  # Initialize an empty set to hold positions for 'who'

    win_comb = [
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # Rows
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # Columns
            {0, 4, 8}, {2, 4, 6}  # Diagonals
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
    if (who == 'X' and hasWon('X')):
        print("You won! Thanks for playing.")
        return True
    elif (who == 'O' and hasWon('O')):
        print("You lost! Thanks for playing.")
        return True
    elif len(played) == 9: # Check for a draw
        print("A draw! Thanks for playing.")
        return True
    else:
        return False

if __name__ == "__main__": 
    init()

    if random.randrange(2) == 1:        # Random draw (50-50) to decide whether the user starts first or the computer starts first.
        print("Player X starts first")
        while True:
            playerNextMove()            # X starts first
            if(terminate('X')): break   # if X won or a draw, print message and terminate
            computerNextMove()          # computer plays O
            if(terminate('O')): break   # if O won or a draw, print message and terminate
    else:
        print("Player O starts first")
        while True:
            computerNextMove()          # O starts first
            if(terminate('O')): break   # if O won or a draw, print message and terminate
            playerNextMove()            # user plays X
            if(terminate('X')): break   # if X won or a draw, print message and terminate
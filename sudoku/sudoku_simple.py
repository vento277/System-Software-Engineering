#student name: Peter Kim
#student number: 18693002

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Initialize a list of numbers that should be present in the subgrid
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Loop through the rows to check if the current cell's value of the column is in the expected list, 'check', 
    # and remove the found number from the list
    for i in range(9):
        if puzzle[i][column] in check: 
            check.remove(puzzle[i][column])
    
    # After checking all cells, determine if the column is valid by seeing if all elements in 'check' have been removed.
    if not check:print("Column " + str(column) + " valid")
    else: print("Column " + str(column) + " not valid")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Initialize a list of numbers that should be present in the subgrid
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Loop through the columns to check if the current cell's value of the row is in the expected list, 'check', 
    # and remove the found number from the list
    for i in range(9):
        if puzzle[row][i] in check: 
            check.remove(puzzle[row][i])
    
    # After checking all cells, determine if the row is valid by seeing if all elements in 'check' have been removed.
    if not check:print("Row " + str(row) + " valid")
    else: print("Row " + str(row) + " not valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Set the starting point of the subgrid by following:
    # where (i, j) == (row, column)
    #   0 -> (0, 0); 1->(0, 3); 2->(0, 6)
    #   3 -> (3, 0); 4->(3, 3); 5->(3, 6)
    #   6 -> (6, 0); 7->(6, 3); 8->(6, 6)
    if subgrid < 3:
        id_i = 0
        id_j = int(subgrid * 3)
    elif 3 <= subgrid < 6:
        id_i = 3
        id_j = int((subgrid-3) * 3)
    else:
        id_i = 6
        id_j = int((subgrid-6) * 3)

    # Initialize a list of numbers that should be present in the subgrid
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Iterate over each cell in the 3x3 subgrid. Loop through rows and columns to check if the current cell's value is in the expected list, 'check', 
    # and remove the found number from the list
    for i in range(3):
        for j in range(3):
            if puzzle[id_i+i][id_j+j] in check: 
                check.remove(puzzle[id_i+i][id_j+j])

    # After checking all cells, determine if the subgrid is valid by seeing if all elements in 'check' have been removed.
    if not check:print("Subgrid " + str(subgrid) + " valid")
    else: print("Subgrid " + str(subgrid) + " not valid")

if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5]
            ]

    testcase = test2   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)
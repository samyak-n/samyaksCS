def initializePuzzle():
    """
    returns puzzle filled with zeros
    """
    return (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]])


def get_cages():
    """
    returns list of cages
    """
    cages = []
    numberOfCages = int(input("Number of cages: "))

    for i in range(numberOfCages):
        cage = input("Cage number %d: " % i).split()  # allows for mulitple
        # input in a single line
        cages.append([int(i) for i in cage])  # addes user input to a list,
        # casting each num as an int, and adds that list to cages
    return cages


def get_cellval(puzzle, cellIndex):
    """
    returns cell value for given cell index
    Arguments:
    puzzle -- (list of lists)
    cellIndex   -- (int) index of cell between 0 and 24
    """
    row = cellIndex // 5
    col = cellIndex % 5

    return (puzzle[row][col])


def update_puzzle(puzzle, cellValue, cellIndex):
    row = cellIndex // 5
    col = cellIndex % 5
    puzzle[row][col] = cellValue
    return (puzzle)


def check_col_val_pre(puzzle, columnIndex):
    """
    returns True if no duplicates in a single column
    Arguments
    puzzle -- (list of lists)
    columnIndex -- (int) between 0 and 4 representing column being checked
    """
    numCounter = dict()
    col = list()
    for i in range(5):
        col.append(puzzle[i][columnIndex])

    for i in col:
        if i < 1:
            continue
        numCounter[i] = numCounter.get(i, 0) + 1  # creates a dictionary
        # representing the number of occurances for each number in a list
    for i in numCounter:
        if numCounter[i] > 1:  # if the number of occurances is greater than one
            return False
    return True


def check_columns_valid(puzzle):
    for col in range(len(puzzle)):
        if not check_col_val_pre(puzzle, col):
            return False
    return True


def check_row_val_pre(puzzle, rowIndex):
    """
    returns True if no duplicates in a single row
    Arguments:
    puzzle -- (list of lists)
    rowIndex    -- (int) between 0 and 4 representing row being checked
    """
    numCounter = dict()
    row = puzzle[rowIndex]

    for i in row:
        if i < 1:
            continue
        numCounter[i] = numCounter.get(i, 0) + 1  # creates a dictionary
        # representing the number of occurances for each number in a list
    for i in numCounter:
        if numCounter[i] > 1:
            return False
    return True


def check_rows_valid(puzzle):
    for row in range(len(puzzle)):
        if not check_row_val_pre(puzzle, row):
            return False
    return True


def check_cages_val_pre(puzzle, cages, cageIndex):
    """
    returns True if sum of cage's cells are less than or equal to the
    required sum
    Arguments :
    puzzle    -- (list of lists)
    cages     -- (list of lists) cage contains: sum, numCells, cageIndex
    cageIndex -- (int) between 0 and numCages
    """
    cage = cages[cageIndex]
    cageSum = cage[0]
    puzzleIndexes = cage[2:]
    puzzleValues = [get_cellval(puzzle, i) for i in puzzleIndexes]
    cageSumTest = 0

    for cellIndex in puzzleIndexes:  # sum of cage
        cageSumTest += get_cellval(puzzle, cellIndex)

    if check_zero(puzzleValues) == True and cageSum == cageSumTest:
        return True
    elif check_zero(puzzleValues) == False and cageSumTest < cageSum:
        return True
    else:
        return False


def check_cages_valid(puzzle, cages):
    for i in range(len(cages)):
        if not check_cages_val_pre(puzzle, cages, i):
            return False
    return True


def check_valid(puzzle, cages):
    """
    returns True if puzzle is still valid for the following: row, columns,
    and cages
    Arguments :
    puzzle    -- (list of lists)
    cages     -- (list of lists) cage contains: sum, numCells, cellIndexes
    """
    if check_cages_valid(puzzle, cages) and check_rows_valid(
            puzzle) and check_columns_valid(puzzle) == True:
        return True
    return False


def check_zero(puzzle):
    """
    returns True if puzzle contains no zeros
    """
    for i in puzzle:
        if i == 0:
            return False
    return True


def print_puzzle(puzzle):
    for row in puzzle:
        for cell in row:
            print(cell, "", end="")
        print()

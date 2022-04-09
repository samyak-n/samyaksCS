from solv_funcs import *


def main():
    puzzle = initializePuzzle()
    cages = get_cages()
    cellIndex = 0
    checks = 0
    backtracks = 0

    while cellIndex < 25:
        cellValue = get_cellval(puzzle, cellIndex) + 1
        puzzle = update_puzzle(puzzle, cellValue, cellIndex)
        #print_puzzle(puzzle)
        checks += 1

        if check_valid(puzzle, cages):  # move to next index
            cellIndex += 1
        else:
            while cellValue >= 5:  # backtracking
                #print_puzzle(puzzle)
                puzzle = update_puzzle(puzzle, 0, cellIndex)
                cellIndex -= 1
                backtracks += 1
                cellValue = get_cellval(puzzle, cellIndex)

    print("\n---Solution---\n")
    print_puzzle(puzzle)
    print()
    print("checks:", checks, "backtracks", backtracks)


if __name__ == '__main__':
    main()

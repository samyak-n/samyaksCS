import solver_funcs


def get_cages():
    cages = []
    number_of_cages = int(input("Number of cages: "))

    for i in range(number_of_cages):
        cage = input("Cage number %d: " % i).split()
        cages.append([int(i) for i in cage])

    return cages


def main():
    puzzle = solver_funcs.init_puzzle()
    cages = get_cages()
    cell_index = 0
    checks = 0
    backtracks = 0

    while cell_index < 25:
        cell_value = solver_funcs.get_cell_val(puzzle, cell_index) + 1
        puzzle = solver_funcs.update_puzzle(puzzle, cell_value, cell_index)
        checks += 1

        if solver_funcs.check_valid(puzzle, cages):
            cell_index += 1
        else:
            while cell_value >= 5:
                puzzle = solver_funcs.update_puzzle(puzzle, 0, cell_index)
                cell_index -= 1
                backtracks += 1
                cell_value = solver_funcs.get_cell_val(puzzle, cell_index)

    print("\n--Solution--\n")
    solver_funcs.print_puzzle(puzzle)
    print()
    print("checks:", checks, "backtracks:", backtracks)


if __name__ == '__main__':
    main()

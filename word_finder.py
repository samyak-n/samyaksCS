import finder_funcs


def print_puzz(puzzle):
    print("Puzzle:\n")
    for i in puzzle:
        print(i)

    print()


def set_up():
    puzzle_str = input()
    words = input().split()

    puzzle = finder_funcs.make_puzzle(puzzle_str)
    reverse_puzzle = finder_funcs.make_reverse_puzzle(puzzle_str)
    reverse_columns = finder_funcs.make_col(reverse_puzzle)
    columns = finder_funcs.make_col(puzzle)
    diagonals = finder_funcs.make_diag(puzzle, columns)

    print_puzz(puzzle)

    return words, puzzle, reverse_puzzle, reverse_columns, columns, diagonals


def main():
    x = set_up()
    finder_funcs.actual_checker(x[0], x[1], x[2], x[3], x[4], x[5])


if __name__ == '__main__':
    main()

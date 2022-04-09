def init_puzzle():
    return (
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]])


def get_cell_val(puzzle, cell_idx):
    row = cell_idx // 5
    col = cell_idx % 5

    return puzzle[row][col]


def update_puzzle(puzzle, cell_val, cell_idx):
    row = cell_idx // 5
    col = cell_idx % 5
    puzzle[row][col] = cell_val

    return puzzle


def check_col_val_pre(puzzle, column_index):
    num_counter = dict()
    col = list()
    for i in range(5):
        col.append(puzzle[i][column_index])

    for i in col:
        if i < 1:
            continue
        num_counter[i] = num_counter.get(i, 0) + 1

    for i in num_counter:
        if num_counter[i] > 1:
            return False
    return True


def check_columns_valid(puzzle):
    for col in range(len(puzzle)):
        if not check_col_val_pre(puzzle, col):
            return False
    return True


def check_row_val_pre(puzzle, row_index):
    num_counter = dict()
    row = puzzle[row_index]

    for i in row:
        if i < 1:
            continue
        num_counter[i] = num_counter.get(i, 0) + 1

    for i in num_counter:
        if num_counter[i] > 1:
            return False
    return True


def check_rows_valid(puzzle):
    for row in range(len(puzzle)):
        if not check_row_val_pre(puzzle, row):
            return False
    return True


def check_cages_val_pre(puzzle, cages, cage_index):
    cage = cages[cage_index]
    cage_sum = cage[0]
    puzzle_indexes = cage[2:]
    puzzle_values = [get_cell_val(puzzle, i) for i in puzzle_indexes]
    cage_sum_test = 0

    for cell_index in puzzle_indexes:  # sum of cage
        cage_sum_test += get_cell_val(puzzle, cell_index)

    if check_zero(puzzle_values) and cage_sum == cage_sum_test:
        return True
    elif check_zero(puzzle_values) is False and cage_sum_test < cage_sum:
        return True
    else:
        return False


def check_cages_valid(puzzle, cages):
    for i in range(len(cages)):
        if not check_cages_val_pre(puzzle, cages, i):
            return False
    return True


def check_valid(puzzle, cages):
    if check_cages_valid(puzzle, cages) and check_rows_valid(
            puzzle) and check_columns_valid(puzzle):
        return True
    return False


def print_puzzle(puzzle):
    for row in puzzle:
        for cell in row:
            print(cell, "", end="")
        print()


def check_zero(puzzle):
    for i in puzzle:
        if i == 0:
            return False
    return True

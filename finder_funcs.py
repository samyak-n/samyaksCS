def make_puzzle(puzzle_str):
    puzzle = []
    for i in range(0, 100, 10):
        puzzle.append(puzzle_str[i:i + 10])
    return puzzle


def make_reverse_puzzle(puzzle_str):
    puzzle_backwards = puzzle_str[::-1]
    reverse_puzzle = []
    for i in range(0, 100, 10):
        reverse_puzzle.append(puzzle_backwards[i:i + 10])
    return reverse_puzzle


def make_col(puzzle):
    columns = []
    for j in range(10):
        column = []
        for i in range(10):
            column.append(puzzle[i][j])
        columns.append("".join(column))
    return columns


def row_check(puzzle, word):
    for r in range(len(puzzle)):
        row = puzzle[r]
        c = row.find(word)
        if word in row:
            return r, c


def col_check(columns, word):
    for c in range(len(columns)):
        column = columns[c]
        r = column.find(word)
        if word in column:
            return r, c


def make_diag(puzzle, columns):
    diagonals = []

    for i in range(len(puzzle[0])):
        diagonal = []
        x = i
        y = 0
        while x < 10:
            diagonal.append(puzzle[y][x])
            x += 1
            y += 1
        diagonals.append("".join(diagonal))

    for i in range(1, 10):
        diagonal = []
        x = 0
        y = i
        while y < 10:
            diagonal.append("".join(columns[x][y]))
            x += 1
            y += 1
        diagonals.append("".join(diagonal))

    return diagonals


def diag_check(diagonals, word):
    for c in range(len(diagonals)):

        if c <= 9:
            row = diagonals[c]
            r = row.find(word)
            if word in row:
                return r, (r + c)

        if c > 9:
            row = diagonals[c]
            r = row.find(word)
            if word in row:
                return c - 9 + r, r


def actual_checker(words, puzzle, reverse_puzzle, reverse_columns, columns,
                   diagonals):

    f = "(FORWARD)"
    d = "(DOWN)"
    dia = "(DIAGONAL)"
    u = "(UP)"
    b = "(BACKWARD)"

    for word in words:
        row = row_check(puzzle, word)
        column = col_check(columns, word)
        read_row = row_check(reverse_puzzle, word)
        read_column = col_check(reverse_columns, word)
        read_diagonal = diag_check(diagonals, word)
        if row is not None:
            print(word + ":", f, "row:", row[0], "column:", row[1])
        elif column is not None:
            print(word + ":", d, "row:", column[0], "column:", column[1])
        elif read_row is not None:
            print(word + ":", b, "row:", 9 - read_row[0], "column:",
                  9 - read_row[1])
        elif read_column is not None:
            print(word + ":", u, "row:", 9 - read_column[0], "column:",
                  9 - read_column[1])
        elif read_diagonal is not None:
            print(word + ":", dia, "row:", read_diagonal[0], "column:",
                  read_diagonal[1])
        elif row is None and column is None and read_row is None and \
                read_column is \
                None:
            print(word + ": word not found")

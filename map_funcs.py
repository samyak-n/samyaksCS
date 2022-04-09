def square_all(numbers):
    newarr = []
    for x in numbers:
        y = x * x
        newarr.append(y)
    return newarr


def add_n_all(numbers, n):
    newarr = [x + n for x in numbers]
    return newarr


def even_or_odd_all(numbers):
    newarr = []
    x = 0
    while x < len(numbers):
        if numbers[x] % 2 == 0:
            newarr.append(True)
        else:
            newarr.append(False)
        x += 1
    return newarr



def are_positive(numbers):
    newarr = []
    for x in numbers:
        if x > 0:
            newarr.append(x)
    return newarr


def are_greater_than_n(numbers, n):
    newarr = [x for x in numbers if x > n]
    return newarr


def are_divisible_by_n(numbers, n):
    newarr = []
    x = 0
    while x < len(numbers):
        if numbers[x] % n == 0:
            newarr.append(numbers[x])
        x += 1
    return newarr


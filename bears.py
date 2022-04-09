import math


def bears(n):
    if n == 42:  # first base case
        return True
    elif n < 42:  # second base case
        return False
    else:
        if (n % 2 == 0) and bears(n / 2):  # checkers
            return True
        if (n % 3 == 0) or (n % 4 == 0) and \
                bears(n - ((n % 10) * math.floor((n % 100) / 10))):
            return True  # checkers for 3/4 case
        if (n % 5 == 0) and bears(n - 42):  # checkers for 5 case
            return True
    return False

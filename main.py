import math


def perm_gen_lex(string):
    if len(string) == 1:
        return [string]
    perm_list = []
    for i in range(len(string)):
        simpler_string = string[:i] + string[i + 1:]
        perm2 = perm_gen_lex(simpler_string)
        for perm in perm2:
            perm_list.append(string[i] + perm)
    return perm_list


def convert_helper(x):  # returns the appropriate remainder, helper function
    if x < 10:
        return str(x)
    elif x == 10:
        return 'A'
    elif x == 11:
        return 'B'
    elif x == 12:
        return 'C'
    elif x == 13:
        return 'D'
    elif x == 14:
        return 'E'
    elif x == 15:
        return 'F'


def convert(num, b):
    quotient = num // b
    remainder = num % b
    if quotient == 0:
        return convert_helper(remainder)
    else:
        return convert(quotient, b) + convert_helper(remainder)


def bears(n):
    if n == 42:
        return True
    elif n < 42:
        return False
    else:
        if (n % 2 == 0) and bears(n / 2):
            return True
        if (n % 3 == 0) or (n % 4 == 0) and \
                bears(n - ((n % 10) * math.floor((n % 100) / 10))):
            return True
        if (n % 5 == 0) and bears(n - 42):
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(perm_gen_lex('a'))
    print(perm_gen_lex('abc'))
    print(perm_gen_lex('abcd'))
    print(convert(0, 2))
    print(bears(250))

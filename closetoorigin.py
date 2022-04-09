import math


def close_to_origin(tuple_set, distance):
    new_tuple_list = []
    for index in tuple_set:
        x = 0
        for index2 in index:
            square = index2 ** 2
            x += square
        ans = math.sqrt(x)
        if ans < distance:
            new_tuple_list.append(index)
    return new_tuple_list


def close_to_oorigin(tuple_list, distance):
    new_tuple_list = []
    for x in tuple_list:
        z = 0
        for y in x:
            square = y ** 2
            z += square
        if math.sqrt(z) < distance:
            new_tuple_list.append(x)
    return new_tuple_list


def starting_letter(list_of_strings):
    new_list = [x[0] for x in list_of_strings]
    return new_list


def starting_letter_looper(list_of_strings):
    new_list = []
    for x in list_of_strings:
        new_list.append(x[0])
    return new_list


def find_2d(list_of_list_of_numbers, number):
    tuple_list = []
    x = 0
    while x < len(list_of_list_of_numbers):
        y = 0
        while y < len(list_of_list_of_numbers[x]):
            if list_of_list_of_numbers[x][y] == number:
                new_tuple = (x, y)
                tuple_list.append(new_tuple)
            y += 1
        x += 1
    return tuple_list




list_num = [[1, 2, 3, 4], [3, 4, 2, 5, 4], [4, 3, 2, 5, 4]]
print(find_2d(list_num, 4))
print(len(list_num))

fruits = ["apple", "Banana", "FRUIT"]
print(starting_letter_looper(fruits))

points = [(4.0, 3.0), (10.3, 7.2), (2.22, 4.1)]
print(close_to_oorigin(points, 5.4))

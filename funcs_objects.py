import math


def distance(p_1, p_2):
    p_3 = math.sqrt((p_1.x - p_2.x) ** 2 + (p_2.y - p_1.y) ** 2)
    return p_3


def circles_overlap(circle_1, circle_2):
    distance1 = math.sqrt((circle_1.center.x - circle_2.center.x) ** 2 + (
            circle_1.center.y - circle_2.center.y) ** 2)
    return distance1 < (circle_1.radius + circle_2.radius)


def distance_circles(circle1, circle2):
    distance_x = abs(circle1.center.x - circle2.center.x)
    distance_y = abs(circle1.center.y - circle2.center.y)
    distance_xy = math.sqrt(distance_x ** 2 + distance_y ** 2)
    distance_inc_radius = distance_xy - circle1.radius - circle2.radius
    return distance_inc_radius


def close_to_origin(tuple_list, distance):
    tuple_set = []
    for tuple1 in tuple_list:
        x = math.sqrt(tuple1[0] ** 2 + tuple1[1] ** 2)
        if x < distance:
            tuple_set.append(tuple1)
    return tuple_set


def find_2d(lists, value):
    tuple_set = []
    for list1 in lists:
        for value1 in list1:
            if value1 == value:
                y = list1.index(value)
                x = lists.index(list1)
                tuple_set.append((x, y))
    return tuple_set


lists = [[1, 2, 3, 4], [-3, 5, 12, 16], [4], [0, 100]]
print(find_2d(lists, 4))

points = [(4.0, 3.0), (10.3, 7.2), (2.22, 4.1)]
print(close_to_origin(points, 5.4))

print(str(5.9), str(5.9))

print(float(4 // 3) + 2.0 * int(3 / 2.0))

print(range(6))
for i in range(5):
    print(i, end=" ")
    for val in range(ord('d'), ord('h'), 2):
        print(chr(val + i), end=" ")
    print()


def disemvowel(str):
    newarray = []
    shitarray = []
    for x in str:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            shitarray.append(x)
        else:
            newarray.append(x)
    newstr = ''.join(newarray)
    return newstr


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array

print(selection_sort([4,3,2,9,5]))


print(disemvowel("yellow"))

import math


def max_101(x, y):
    if x > y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    if x >= y and x > z:
        return x
    elif y > x and y >= z:
        return y

    else:
        return z


def rental_late_fee(days):
    days = int(days)
    if days <= 0:
        return 0
    elif days <= 9:
        return 5
    elif days <= 15:
        return 7
    elif days <= 24:
        return 19
    elif days > 24:
        return 100


#num1 = input("put in yo numbaz")
#num2 = input("put in yo numbaz")
#num3 = input("put in yo numbaz")

#print(max_101(num1, num2))
#print(max_of_three(num1, num2, num3))
#print(rental_late_fee(num1))

import math


def pounds_to_kg(pounds):
    kg = pounds * 0.453592
    return kg


def get_mass_object(letter):
    object_weight = [0.1, 1.0, 3.0, 5.3, 9.07]
    if letter == "t":
        return object_weight[0]
    elif letter == "p":
        return object_weight[1]
    elif letter == "r":
        return object_weight[2]
    elif letter == "g":
        return object_weight[3]
    elif letter == "l":
        return object_weight[4]
    else:
        return 0.0


def get_velocity_object(distance):
    velocity_object = math.sqrt((9.8 * float(distance)) / 2)
    return velocity_object


def get_velocity_skater(mass_skater, mass_object, velocity_object):
    velocity_skater = (mass_object * velocity_object) / mass_skater
    return velocity_skater

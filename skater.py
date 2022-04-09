import funcs


def main():
    pounds = float(input("How much do you weigh (pounds)? "))
    distance = float(input("How far away is your professor (meters)? "))
    letter = input("Will you throw a rotten (t)omato, banana cream (p)ie,"
                   " (r)ock, (l)ight saber, or lawn (g)nome? ")

    mass_skater = funcs.pounds_to_kg(pounds)
    mass_object = funcs.get_mass_object(letter)
    velocity_object = funcs.get_velocity_object(distance)
    velocity_skate = funcs.get_velocity_skater(mass_skater, mass_object,
                                               velocity_object)
    velocity_skate_format = (format(velocity_skate, ".3f"))

    nt = "\nNice throw!"

    if mass_object <= 0.1:
        print(nt, "You're going to get an F!")
    elif 0.1 < mass_object <= 1.0:
        print(nt, "Make sure your professor is OK.")
    else:
        if distance < 20:
            print(nt, "How far away is the hospital?")
        else:
            print(nt, "RIP professor.")

    print("Velocity of skater:", velocity_skate_format, "m/s")

    if velocity_skate < 0.2:
        print("My grandmother skates faster than you!")
    elif velocity_skate >= 1.0:
        print("Look out for that railing!!!")


if __name__ == '__main__':
    main()

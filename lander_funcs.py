def show_welcome():
    print("\nWelcome aboard the Lunar Module Flight Simulator\n")
    print(
        "   To begin you must specify the LM's initial altitude\n   and fuel "
        "level.  To simulate the actual LM "
        "use\n   values of 1300 meters and 500 liters, respectively.")
    print("\n   Good luck and may the force be with you!")


def get_altitude():
    altitude = int(input("Enter the initial altitude of the LM (in meters): "))
    while altitude <= 0 or altitude >= 10000:
        print(
            "ERROR: Altitude must be between 1 and 9999, inclusive, please "
            "try again")
        altitude = int(
            input("Enter the initial altitude of the LM (in meters): "))
    return altitude


def get_fuel():
    fuel_amount = int(input(
        "Enter the initial amount of fuel on board the LM (in liters): "))
    while fuel_amount <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel_amount = int(input(
            "Enter the initial amount of fuel on board the LM (in liters): "))
    return fuel_amount


def display_lm_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
    print("Elapsed Time:" + '{:5d}'.format(elapsed_time) + " s")
    print("        Fuel:" + '{:5d}'.format(fuel_amount) + " l")
    print("        Rate:" + '{:5d}'.format(fuel_rate) + " l/s")
    print("    Altitude:" + '{:8.2f}'.format(altitude) + " m")
    print("    Velocity:" + '{:8.2f}'.format(velocity) + " m/s")


def get_fuel_rate(current_fuel):
    num = int(input(
        "\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, "
        "9=max thrust): "))
    while num < 0 or num > 9:
        print("ERROR: Fuel rate must be between 0 and 9, inclusive")
        num = int(input(
            "\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, "
            "9=max thrust): "))
    if num < current_fuel:
        return num
    elif num >= current_fuel:
        return current_fuel


def display_lm_landing_status(velocity):
    if 0 >= velocity >= -1:
        print("Status at landing - The eagle has landed!")
    elif -1 >= velocity >= -10:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")


def update_acceleration(gravity, fuel_rate):  # is this the same fuel rate
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return acceleration


def update_altitude(altitude, velocity, acceleration):
    new_altitude = altitude + velocity + acceleration / 2
    if new_altitude >= 0:
        return new_altitude
    else:
        return 0


def update_velocity(velocity, acceleration):
    new_velocity = velocity + acceleration
    return new_velocity


def update_fuel(fuel, fuel_rate):
    new_fuel = fuel - fuel_rate
    return new_fuel

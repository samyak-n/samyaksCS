def weight_on_planets():
    weight_earth = input("What do you weigh on Earth? ")
    weight_earth = int(weight_earth)
    weight_mars = weight_earth * 0.38
    weight_jup = weight_earth * 2.53
    print("\nOn Mars you would weigh", weight_mars, "pounds. \n"
                                                    "On Jupiter you would weigh", weight_jup, "pounds. ")
    return weight_mars, weight_jup


# NOTE: This means if the code is run as `python3 planetes.py`, run the
# main function.  If the code is merely imported, don't do anything.
if __name__ == '__main__':
    weight_on_planets()

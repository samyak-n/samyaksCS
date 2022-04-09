import lander_funcs


def main():
    lander_funcs.show_welcome()
    print()

    altitude = lander_funcs.get_altitude()
    fuel_amount = lander_funcs.get_fuel()
    elapsed_time = 0
    velocity = 0.00
    fuel_rate = 0
    gravity = 1.62
    print()

    print('LM state at retrorocket cutoff')
    lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                  fuel_amount, fuel_rate)

    while fuel_amount > 0 and altitude > 0:
        elapsed_time += 1
        fuel_rate = lander_funcs.get_fuel_rate(fuel_amount)
        acceleration = lander_funcs.update_acceleration(gravity, fuel_rate)
        fuel_amount = lander_funcs.update_fuel(fuel_amount, fuel_rate)
        altitude = lander_funcs.update_altitude(altitude, velocity,
                                                acceleration)
        velocity = lander_funcs.update_velocity(velocity, acceleration)
        if altitude > 0:
            if fuel_amount > 0:
                lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                              fuel_amount,
                                              fuel_rate)
        if altitude <= 0:
            print('')
            print('LM state at landing/impact')
            altitude = 0
            lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                          fuel_amount,
                                          fuel_rate)
            print('')
            lander_funcs.display_lm_landing_status(velocity)
    while altitude > 0:
        print('OUT OF FUEL - ' + 'Elapsed Time:' + '{:4d}'.format(
            elapsed_time) + ' Altitude:' + '{:8.2f}'.format(
            altitude) + ' Velocity:' + '{:8.2f}'.format(velocity))
        fuel_rate = 0
        elapsed_time += 1
        acceleration = lander_funcs.update_acceleration(gravity, fuel_rate)
        altitude = lander_funcs.update_altitude(altitude, velocity,
                                                acceleration)
        velocity = lander_funcs.update_velocity(velocity, acceleration)
        if altitude <= 0:
            print('')
            print('LM state at landing/impact')
            elapsed_time += 0
            fuel_amount = 0
            fuel_rate = 0
            acceleration = lander_funcs.update_acceleration(gravity, fuel_rate)
            altitude = 0
            lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                          fuel_amount,
                                          fuel_rate)
            print('')
            lander_funcs.display_lm_landing_status(velocity)


if __name__ == '__main__':
    main()

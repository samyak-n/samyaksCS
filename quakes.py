import quake_funcs
import sys
import utils


def main():
    in_file = open(sys.argv[1], 'r')
    quakes = quake_funcs.read_quakes_from_file(in_file)
    in_file.close()
    filter_quakes = quakes[:]

    choice = ''
    while choice != 'q':
        print('Earthquakes:')
        print('------------')
        for quake in filter_quakes:
            print(quake)

        print('\nOptions:')
        print('  (s)ort')
        print('  (f)ilter')
        print('  (n)ew quakes')
        print('  (q)uit\n')

        choice = input('Choice: ').lower()
        if choice == 's':
            sort_choice = input('Sort by (m)agnitude, (t)ime, ' +
                                '(l)ongitude, or l(a)titude? ').lower()
            quakes = quake_funcs.sort_quakes(quakes, sort_choice)
            filter_quakes = quakes[:]

        elif choice == 'f':
            filter_choice = input('Filter by (m)agnitude ' +
                                  'or (p)lace? ').lower()
            if filter_choice == 'm':
                low = float(input('Lower bound: '))
                high = float(input('Upper bound: '))
                filter_quakes = quake_funcs.filter_by_mag(quakes, low, high)
            if filter_choice == 'p':
                word = input('Search for what string? ')
                filter_quakes = quake_funcs.filter_by_place(quakes, word)

        elif choice == 'n':
            json = utils.get_json('https://earthquake.usgs.gov/' +
                                  'earthquakes/feed/v1.0/summary/' +
                                  '1.0_hour.geojson')
            new_count = 0
            for feature in json['features']:
                new_quake = quake_funcs.quake_from_feature(feature)
                if new_quake not in quakes:
                    new_count += 1
                    quakes.append(new_quake)
            filter_quakes = quakes[:]
            if new_count > 0:
                print('\nNew quakes found!!!')

        else:
            filter_quakes = quakes[:]

        print()

    out_file = open(sys.argv[1], 'w')
    for quake in quakes:
        out_file.write(repr(quake) + '\n')
    out_file.close()


if __name__ == '__main__':
    main()

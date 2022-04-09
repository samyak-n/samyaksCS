from sys import argv


def main():
    if len(argv) == 1 or len(argv) > 3:
        print('usage: parse_file.py [-s] file_name')
        exit()
    elif len(argv) == 3 and '-s' not in argv:
        print('usage: parse_file.py [-s] file_name')
        exit()
    else:
        if len(argv) == 2:
            file_name = argv[1]
        else:
            argv.pop(argv.index('-s'))
            file_name = argv[1]
            argv.append('-s')
        try:
            in_file = open(file_name, 'r')
        except IOError:
            print("Unable to open", file_name)
            exit()

    ints = 0
    floats = 0
    other = 0
    total = 0
    for line in in_file:
        splitter = line.split()
        for x in splitter:
            try:
                float(x)
                isfloat = True
            except ValueError:
                isfloat = False
            if x.isdigit():
                ints += 1
                total += int(x)
            elif isfloat:
                floats += 1
                total += float(x)
            else:
                other += 1

    in_file.close()
    print('Ints: %d' % ints)
    print('Floats: %d' % floats)
    print('Other: %d' % other)
    if len(argv) == 3:
        print('Sum: %.2f' % total)


if __name__ == '__main__':
    main()

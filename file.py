file = open('in.txt', 'r')

file_cursor = 0
for line in file:
    print('Line %d (%d chars): %s' % (
        file_cursor, len(line.strip()), line.strip()))
    file_cursor += 1

file.close()

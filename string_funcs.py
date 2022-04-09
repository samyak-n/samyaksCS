def str_rot_13(statement):
    new_list = []
    for i in statement:
        if (ord('a') <= ord(i) <= ord('z')) or \
                (ord('A') <= ord(i) <= ord('Z')):
            if ord('a') <= ord(i) <= ord('z'):
                if ord(i) < ord('n'):
                    char_val = ord(i) + 13
                    new_list.append(chr(char_val))
                else:
                    char_val = ord(i) - 13
                    new_list.append(chr(char_val))
            else:
                if ord(i) < ord('N'):
                    char_val = ord(i) + 13
                    new_list.append(chr(char_val))
                else:
                    char_val = ord(i) - 13
                    new_list.append(chr(char_val))
        else:
            new_list.append(i)
    new_str = ''.join(new_list)
    return new_str


def str_translate_101(s2, let1, let2):
    new_str = ''
    x = list(map(lambda y: new_str + let2 if y == let1 else new_str + y, s2))
    return ''.join(x)

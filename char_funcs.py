def is_lower_101(char):
    if 97 <= ord(char) <= 122:
        return True
    else:
        return False


def char_rot_13(char):
    x = ord(char)
    y = 13 + x
    if 65 <= x <= 122:
        if x >= 97:
            if y > 122:
                z = y - 122
                new_char = 96 + z
                return chr(new_char)
            else:
                return chr(y)
        else:
            if y > 90:
                z = y - 90
                new_char = 64 + z
                return chr(new_char)
            else:
                return chr(y)
    else:
        return char







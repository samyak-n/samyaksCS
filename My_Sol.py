def bin_search(target, low, high, int_list):  # must use recursion
    if target in int_list:
        if int_list[low] == target:
            print(low)
            return low
        else:
            return bin_search(target, low + 1, high, int_list)
            # print(4)
    else:
        raise ValueError
def sum2(input_list):
    count = 0
    for x in input_list:
        count += x
    return count


def index_of_smallest(input_list):
    index = 0
    if len(input_list) > 0:
        index_smallest = 0
        count = input_list[0]
        for x in input_list:
            if x < count:
                count = x
                index_smallest = index
            index += 1
        return index_smallest
    else:
        return -1


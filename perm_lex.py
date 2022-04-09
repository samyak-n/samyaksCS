def perm_gen_lex(string):
    if len(string) == 1:  # base case
        return [string]
    perm_list = []  # empty list
    for i in range(len(string)):  # iter over list
        simpler_string = string[:i] + string[i + 1:]  # switch letters
        perm2 = perm_gen_lex(simpler_string)  # recursive to find perms
        for perm in perm2:  # add to perm list
            perm_list.append(string[i] + perm)
    return perm_list  # return perm list

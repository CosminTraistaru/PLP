def my_map(func, *iterables):

    def set_none(max_len, mod_list):
        for x in xrange(0, max_len):
            try:
                mod_list[x]
            except IndexError:
                mod_list.append(None)

    if not iterables:
        raise TypeError("mymap() requires at least two args")

    nr_of_arg = max([len(x) for x in iterables])
    if len(iterables) > 1:
        for i in xrange(0, len(iterables)):
            set_none(nr_of_arg, iterables[i])

        list_of_lists_to_pass_to_func = []
        for i in xrange(0, nr_of_arg):
            list_of_lists_to_pass_to_func.append(
                [iterables[j][i] for j in xrange(0, len(iterables))])
        results = [func(x) for x in list_of_lists_to_pass_to_func]
    else:
        results = [func(x) for x in iterables[0]]
    return results



a = [(1, 9), (2, 5)]
b = [1, 2, 5, 4, 6, 7]
c = [1, 2, 24, 664, 6, 99, 5, 4, 5, 5, 5, 5, 5]

print my_map(max, b, c)
print map(max, b, c)

print my_map(min, b, c)
print map(min, b, c)




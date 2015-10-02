def my_reduce(func, iterable, initializer=None):
    result = initializer
    for it in iterable:
        result = func(result, it)
    return result


print reduce(lambda x, y: x*y, [1, 2, 3, 4, 5], 1)
print my_reduce(lambda x, y: x*y, [1, 2, 3, 4, 5], 1)
def my_filter(func, iterable):
    result = [i for i in iterable if func(i)]
    return result


b = []
a = [3, 5, 7, 8, 4, 4, 2, 5, 7, 5]

print filter(lambda x: x < 5, b)
print my_filter(lambda x: x < 5, b)

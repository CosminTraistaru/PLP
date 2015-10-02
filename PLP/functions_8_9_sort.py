def my_sort(values):

    for i in xrange(0, len(values)-1):
        if not values[i] < values[i+1]:
            values[i], values[i+1] = values[i+1], values[i]
            for j in xrange(0, i):
                if not values[i-j-1] < values[i-j]:
                    values[i-j-1], values[i-j] = values[i-j], values[i-j-1]


def search(value, received_list):
    for item in received_list:
        if item == value:
            return True
    return False


if __name__ == '__main__':
    a = [99, 2, 6, 3, 99,  1, 'c', 34, 5, 1, 2, 3, 4, 5, 6, 'a', 'b', 0]
    my_sort(a)
    print a
    print search('x', a)

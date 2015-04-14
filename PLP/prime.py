import os


def prime(num):
    if num < 2:
        return False
    if num in [2, 3]:
        return True
    for n in xrange(2, num-1):
        if num % n == 0:
            return False
    return True


if __name__ == '__main__':
    print "Give me your name and money!"
    read = os.read(0, 10)
    print prime(int(read))

    print "All the numbers"
    read = os.read(0, 10)
    numbers = range(1, int(read))
    map(prime, numbers)



import os


def prime(num):
    # if num < 2:
    #     return False
    # if num in (2, 3):
    #     return True
    # for n in xrange(2, num-1):
    #     if num % n == 0:
    #         return False
    # # return True
    return all(num % n != 0 for n in xrange(2, num-1))

if __name__ == '__main__':
    print "Give me your name and money!"
    read = os.read(0, 10)
    try:
        num = int(read)
    except ValueError:
        print "Not a number! Bye!"
    print prime(num)

    print "All the numbers"
    read = os.read(0, 10)
    try:
        num = int(read)
    except ValueError:
        print "Not a number! Bye!"
    print map(prime, xrange(1, num))

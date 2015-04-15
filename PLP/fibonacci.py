# xn = xn-1 + xn-2
#     f0 = 0
#     f1 = 1
#     f2 = 1


def fibonacci_iter(num):
    fib = []
    for n in xrange(0, num):
        if n == 0:
            fib.append(0)
        elif n in [1, 2]:
            fib.append(1)
        else:
            fib.append(fib[n-1] + fib[n-2])
    print fib


def fibonacci_rec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        fib = fibonacci_rec(num - 1) + fibonacci_rec(num - 2)
    return fib

if __name__ == '__main__':
    fibonacci_iter(19)
    fib_seq = [fibonacci_rec(n) for n in xrange(0, 19)]
    print fib_seq
import sys
sys.setrecursionlimit(100000)


def memoization(f):

    class MemoDict(dict):

        __slots__ = ()

        def __missing__(self, key):
            self[key] = ret = f(key)
            return ret

    return MemoDict().__getitem__


@memoization
def fibonacci_rec(num):
    if num < 2:
        return num
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


fibonacci_rec(3000)
fibonacci_rec(3000)
fibonacci_rec(3000)
fibonacci_rec(3000)
fibonacci_rec(3000)

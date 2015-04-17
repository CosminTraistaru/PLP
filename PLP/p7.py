if __name__ == '__main__':
    num = 7
    l = filter(lambda x: (x * x - 1) % 3 != 0, range(0, num))
    print l
    print reduce(lambda x, y: x + y, l)

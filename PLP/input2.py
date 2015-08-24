from prime import prime


with open('dest.txt', 'w+') as f:
    for x in xrange(1, 100):
        if prime(x):
            f.write('{}\n'.format(x))

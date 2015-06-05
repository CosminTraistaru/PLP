import os


if __name__ == '__main__':
    print "Give me your name and money!"
    read = os.read(0, 20)
    print "".join(reversed(read)).upper()

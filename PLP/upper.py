import os


def reverse_upper_print(name):
    letter_list = [letter for letter in name]
    letter_list.reverse()
    return "".join(letter_list).upper()


if __name__ == '__main__':
    print "Give me your name and money!"
    read = os.read(0, 20)
    print reverse_upper_print(read)
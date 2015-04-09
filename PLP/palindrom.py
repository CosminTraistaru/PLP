
def check_palindrome(num):
    list_of_num = []
    original_number = num
    while num % 10 > 0:
        list_of_num.append(num % 10)
        num /= 10
    number_of_elements = len(list_of_num)
    for i in xrange(0, len(list_of_num)/2):
        if not list_of_num[i] == list_of_num[number_of_elements - i - 1]:
            print "{} not a pal".format(original_number)
        else:
            print "{} is palindrome".format(original_number)


if __name__ == "__main__":
    number = 123456787654321
    check_palindrome(number)

    numbers = range(1, 1000)
    map(check_palindrome, numbers)  # all palindrome lower than 1000
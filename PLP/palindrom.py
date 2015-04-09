

def check_palindrome(num):
    list_of_num = []
    while num % 10 > 0:
        list_of_num.append(num % 10)
        num /= 10
    number_of_elements = len(list_of_num)
    for i in xrange(0, len(list_of_num)/2):
        if not list_of_num[i] == list_of_num[number_of_elements - i - 1]:
            return False


if __name__ == "__main__":
    number = 123456787654321
    if check_palindrome(number) is not False:
        print "{number} is a palindrome".format(number=number)
    else:
        print "not"

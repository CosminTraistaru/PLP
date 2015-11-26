
def check_palindrome(num):
    list_of_num = []

    while num % 10 > 0:
        list_of_num.append(num % 10)
        num /= 10
    # check that the list of digits is the same with the reversed one
    if list_of_num == list_of_num[::-1]:
        print 'pal'
    else:
        print 'no pal'


if __name__ == "__main__":
    number = 123456787654321
    check_palindrome(number)

    numbers = range(1, 1000)
    map(check_palindrome, numbers)  # all palindrome lower than 1000
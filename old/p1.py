#!/usr/bin/python 

# Problem 1:
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a 
# single line.


def numbers(min, max):
    result = []

    for number in xrange(min, max):
        if number % 7 == 0 and number % 5 is not 0:
            result.append(number)
    return result


printed_result = ""
for number in  numbers(2000, 3200):
    printed_result = "{} {},".format(printed_result, number)
print printed_result[:-1]


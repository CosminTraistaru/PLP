#!/usr/bin/python 

##Problem 1:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

result = ""

for number in range(2000, 3001):
    if number % 7 == 0 and number % 5 is not 0:
        result += str(number) + ", "
print result[:-2]


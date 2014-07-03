#!/usr/bin/python

#     Problem 4:
# Write a program that accepts a sentence and calculate the number of 
# letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


from collections import Counter


def get_string():
    text = raw_input("Enter input: ")
    return text


def count(text):
    print "Digits {}".format(Counter(map(str.isdigit, text))[1])
    print "Letters {}".format( Counter(map(str.isalpha, text))[1])
 #    return [letters, digits]



text = get_string()
counted = count(text)
# print "Letters {}".format(counted[0])
# print "Digits {}".format(counted[1])


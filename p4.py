#!/usr/bin/python

#     Problem 4:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def getString():
    text = raw_input("Enter input: ")
    return text


def count(text):
    letters = 0
    digits = 0
    for character in text:
        if character.isalpha():
            letters += 1
        if character.isdigit():
            digits += 1
    return [letters, digits]


text = getString()
counted = count(text)
print "Letters {}".format(counted[0])
print "Digits {}".format(counted[1])


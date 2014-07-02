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


def count_letters_and_digits(text):
    letters = 0
    digits = 0
    for character in text:
        if character.isalpha():
            letters += 1
        elif character.isdigit():
            digits += 1

    print "LETTERS {}".format(str(letters))
    print "DIGITS {}".format(str(digits))


def count_letters(text):
    letters = 0
    for character in text:
        if character.isalpha():
            letters += 1
    return letters


def count_digits(text):
    digits = 0
    for character in text:
        if character.isdigit():
            digits += 1
    return digits


text = getString()
count_letters_and_digits(text)

print "Digits {}".format(count_digits(text))
print "Letters {}".format(count_letters(text))


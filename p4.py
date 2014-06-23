#!/usr/bin/python

#     Problem 4:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


class ProblemFour:

    def getString(self):
        text = raw_input("Enter input: ")
        return text

    def count_letters_and_digits(self, text):
        letters = 0
        digits = 0
        for character in text:
            if character.isalpha():
                letters += 1
            else:
                if character.isdigit():
                    digits += 1
        
        print "LETTERS " + str(letters)
        print "DIGITS " + str(digits)


x = ProblemFour()
text = x.getString()
x.count_letters_and_digits(text)


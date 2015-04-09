#!/usr/bin/python

#  Problem 2:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

# Hints:
# Use __init__ method to construct some parameters


class ProblemTwo(object):
    
    def __init__(self):
        self.message = ""

    def get_string(self):
        self.message = raw_input("Enter a text: ")
        return self.message

    def print_string(self, message):
        print self.message.upper()


x = ProblemTwo()
x.print_string(x.get_string())


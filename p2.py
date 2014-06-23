#!/usr/bin/python

#  Problem 2:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

# Hints:
# Use __init__ method to construct some parameters

text = ""

class ProblemTwo:
    
    def __init__(self):
        self.message = ""

    def getString(self):
        self.message = raw_input("Enter a text: ")
        return self.message

    def printString(self, message):
        print self.message.upper()


x = ProblemTwo()
text = x.getString()
x.printString(text)


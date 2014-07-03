#!/usr/bin/python

#     Problem 5:
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
#
# Hints:
# Use list[index] notation to get a element from a list


from itertools import product


subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey", "Football"]

for sentence in product(subject, verb, obj):
    print ' '.join(sentence)


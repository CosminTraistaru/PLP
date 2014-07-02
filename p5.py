#!/usr/bin/python

#     Problem 5:
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
#
# Hints:
# Use list[index] notation to get a element from a list


subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey", "Football"]

for i in range(len(subject)):
    for j in range(len(verb)):
        for k in range(len(obj)):
            print "{} {} {}".format(str(subject[i]), str(verb[j]),  str(obj[k]))


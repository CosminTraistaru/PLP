#!/usr/bin/python

#     Problem 6:
# Write a program which reads from a text file (text file to be provided) 
# and returns individual words in lowercase and stripped from digits and 
# punctuation. It should return a list of words.

#     Problem 6.1
# Make a function which takes as input the list of words, and returns a 
# dict that has as a key the word and as value the number of occurrences.

#     Problem 6.2
# Return the word with the most occurrences


import re
from collections import Counter


def read_text():
    words = re.findall(r'\w+', open('foo.txt').read().lower())
    return words

def occurence_dict(list_of_words):
    dict = Counter(list_of_words).most_common()
    print dict
    return dict

def most_occurence(list_of_words):
    mo = Counter(list_of_words).most_common(1)
    print mo
    return mo


words = read_text() # 6
occurence_dict(words) # 6.1
most_occurence(words) # 6.2


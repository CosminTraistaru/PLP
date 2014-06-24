#!/usr/bin/python

#     Problem 6:
# Write a program which reads from a text file (text file to be provided) and returns individual words in lowercase and stripped from digits and punctuation. It should return a list of words.

#     Problem 6.1
# Make a function which takes as input the list of words, and returns a dict that has as a key the word and as value the number of occurrences.

#     Problem 6.2
# Return the word with the most occurrences

def readText():
    
    final_list = []
    f = open('foo.txt', 'rU')
    text = f.read()
    f.close()
    lower_text = text.lower()
    lower_stripped_text = lower_text.strip()
    lower_stripped_splited_text = lower_stripped_text.split(' ')

    for word in lower_stripped_splited_text:
        word = word.translate(None, '`~!?,.:;"-()0123456789\n\xe2\x80\x9d\x99s\x9c\x94')
        if word is not '':
            final_list.append(word)
    print final_list
    return final_list


def occurenceDict(list_of_words):
    dict = {}
    list_len = len(list_of_words)
    for i in range(list_len):
        if list_of_words[i] in dict.keys():
            dict[list_of_words[i]] = dict[list_of_words[i]] + 1
        else:
            dict[list_of_words[i]] = 1
    print dict
    return dict


def mostOccurences(dict):
    mo_word = ''
    mo_value = 0
    for key in dict.keys():
        if dict[key] > mo_value:
            mo_value = dict[key]
            mo_word = key
    print mo_word + ' ' + str(mo_value) 


mostOccurences(occurenceDict(readText()))


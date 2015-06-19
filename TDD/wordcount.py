from collections import defaultdict

def word_count(message):
    dict = defaultdict(int)
    list_of_words = message.replace('  ', '').replace('\n', ' ').split(' ')

    for word in list_of_words:
        dict[word] += 1
    return dict
"Algorithm to count words in input file"

import string

from operator import itemgetter
from sys import argv

script, filename = argv

def wordcount(filename):
    f = open(filename)
    word_counter = {}
    punctuation = string.punctuation + ' '

    for line in f:
        words = line.split()

        for word in words:
            word = word.strip(punctuation).lower()
            if not word_counter.get(word):
                word_counter[word] = 1
            else:
                word_counter[word] +=1
    return word_counter


def sort_dict_freq(my_dict):
    "Sorts dictionary in descending order of value and alphabetical within values"

    sorted_by_freq_then_letter = sorted(my_dict.items(), key = itemgetter(1,0), reverse = False)
    for item in sorted_by_freq_then_letter:
        word = item[0]
        numb_times = item[1]
        print "%s appears %r times" % (word,numb_times)


sort_dict_freq(wordcount(filename))

"Algorithm to count words in input file"

import string


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
    #close file
    return word_counter


def sort_dict_freq(my_dict):
    "Sorts dictionary in descending order of value and alphabetical within values"
    my_dict = my_dict.items()

    my_dict_into_reverse_tuple = []
    for i in range(len(my_dict)):
        word = my_dict[i][0]
        count = my_dict[i][1]
        my_dict_into_reverse_tuple.append((count, word))

    sorted_out_of_place = sorted(my_dict_into_reverse_tuple)

    for i in range(len(sorted_out_of_place)):
        print sorted_out_of_place[i][1], sorted_out_of_place[i][0]


sort_dict_freq(wordcount(filename))

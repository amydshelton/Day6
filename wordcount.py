"Algorithm to count words in input file"

def wordcount(filename):
    f = open(filename)
    word_counter = {}

    for line in f:
        line = line.strip()
        words =  line.split()

        for word in words:
            word = word.lower()
            if word_counter.get(word, False) == False:
                word_counter[word] = 1
            else:
                word_counter[word] +=1

    return word_counter


print wordcount("StIves.txt")

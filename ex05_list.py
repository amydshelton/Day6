"Exercise 5 - count each letter in a file"

from sys import argv
# import string

script, filename = argv


# def make_letter_list():
#     alpha_list = []
#     alphabet = string.ascii_lowercase

#     for letter in alphabet:
#         alpha_list.append(letter)
#     return alpha_list

def open_and_read_file(filename):
    f = open(filename)
    file_text = f.read().lower()
    count_list = [0] * 26


    for char in file_text:
        if ord(char) > 96 and ord(char) < 123:
            count_list[ord(char)-97] += 1
        # if char in letter_list:
        #     position = letter_list.index(char)
        #     count_list[position] += 1
        # else:
        #     continue


    # while 0 in count_list:
    #     count_list.remove(0)

    return count_list


def main():
    print open_and_read_file(filename)


if __name__ == "__main__":
    main()


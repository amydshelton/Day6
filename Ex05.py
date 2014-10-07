"Exercise 5 - count each letter in a file"

from sys import argv

script, filename = argv

def open_and_read_file(filename):
    letter_dict = {}

    f = open(filename)
    file_text = f.read().lower()

    for char in file_text:
        letter_dict[char] = letter_dict.get(char, 0) + 1
       # print char
    return letter_dict
    # print f

def sort_key_and_print(dictionary):
    for character, count in sorted(dictionary.items()):
        print count

def main():
    open_and_read_file(filename)
    letters = open_and_read_file(filename)
    sort_key_and_print(letters)

    

if __name__ == "__main__":
    main()


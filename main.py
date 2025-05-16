from stats import get_num_words
from stats import get_num_each_char
from stats import sort_dict
import sys

"""
Args:
    filepath: The relative path to a .txt file

Returns:
    The .txt file as a string
"""
def get_book_text(filepath):
    file_as_string = ""
    with open(filepath) as f:
        file_contents = f.read()
        file_as_string += file_contents
    return file_as_string

def main():
    #path_to_file = "./books/frankenstein.txt"
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_to_print = get_book_text(sys.argv[1])
    #print(text_to_print)

    count_of_words = get_num_words(text_to_print)
    #print(count_of_words, "words found in the document")

    num_each_char = get_num_each_char(text_to_print)
    #print(num_each_char)
    sort_num_each_char = sort_dict(num_each_char)      

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", count_of_words, "total words")
    print("--------- Character Count -------")
    for char, value in sort_num_each_char.items():
        if char.isalpha() == True:
            print(f"{char}: {value}")
    print("============= END ===============")

main()
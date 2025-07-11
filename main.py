import sys
from stats import *


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    num_words = get_word_count(get_book_text(book))
    letter_counts = get_letter_counts(get_book_text(book))
    sorted_list = sort_letter_count_dict(letter_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main()
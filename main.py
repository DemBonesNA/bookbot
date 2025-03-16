from stats import (
    word_count, 
    character_count,
    chars_dict_to_sorted_list
)

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents

def full_text():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    main_count = word_count("books/frankenstein.txt")
    print(f"{main_count} words found in the document")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = char_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def char_count_main():
    main_count = word_count("books/frankenstein.txt")
    print(f"{main_count} words found in the document")

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
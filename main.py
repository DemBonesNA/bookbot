from stats import (
    word_count, 
    character_count
    chars_dict_to_sorted_list
)

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents

def full_text():
    text = get_book_text("books/frankenstein.txt")
    print(text)

def main():
    main_count = word_count("books/frankenstein.txt")
    print(f"{main_count} words found in the document")

def char_count_main():
    char_count = character_count("books/frankenstein.txt")
    print(char_count)

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
main(), char_count_main()
    
   
        
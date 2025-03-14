from stats import word_count, character_count

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

main(), char_count_main()
    
   
        
def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents

def main():
    main_files = get_book_text("books/frankenstein.txt")
    print(main_files)

main()
    
   
        
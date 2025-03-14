def word_count(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
        words = file_contents.split()
    return (len(words))
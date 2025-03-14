def word_count(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
        words = file_contents.split()
    return (len(words))

def character_count(file_path):
    char_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
        lowercase_contents = file_contents.lower()
        base_data = list(lowercase_contents)
        for i in base_data:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1
    return char_dict


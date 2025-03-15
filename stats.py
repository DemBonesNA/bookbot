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

def bookbot_report(chars_dict):
    return chars_dict["num"]
   
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


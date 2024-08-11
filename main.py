def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print_char_report(file_contents)

def word_count(content):
    return len(content.split())

def char_count(content):
    char_dict = {}
    content_copy = content
    words = content_copy.split()
    for word in words:
        lowered = word.lower()
        for char in lowered:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] = char_dict[char] + 1
                else:
                    char_dict[char] = 1
    return char_dict

def convert_to_list_of_dict(dict):
    res = []
    for key in dict:
        res.append({"char": key, "num": dict[key]})
    return res

def sort_on(dict):
    return dict["num"]

def print_char_report(content):
    char_list = convert_to_list_of_dict(char_count(content))
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(content)} words found in the document \n")

    for item in char_list:
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---\n")

main()
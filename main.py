from stats import get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as f:
            file_contents = f.read()
        report(file_contents)

def number_of_characters(input_string):
    number_of_char = {}
    lowered_string = input_string.lower()

    for s in lowered_string:
        if s in number_of_char:
            number_of_char[s] += 1
        else:
            number_of_char[s] = 1
    return number_of_char

def report(text_file):
    word_count = get_num_words(text_file)
    num_of_chars = number_of_characters(text_file)
    list_of_dict = []

    for key in num_of_chars:
        if key.isalpha():
            list_of_dict.append({key: num_of_chars[key]})
    #sort dictionary, descending by value
    sorted_list = sorted(list_of_dict, key=lambda x: list(x.values())[0], reverse=True)
    
    #Print report
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in sorted_list:
        for key in item.keys():
            print(f"- '{key}: {item[key]}'")
    
    print("--- End report ---")
    
        
main()
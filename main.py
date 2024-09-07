def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(number_of_words(file_contents))
    #number_of_characters(file_contents)
    report(file_contents)

def number_of_words(input_text):
    words = input_text.split()
    return len(words)

def number_of_characters(input_string):
    number_of_char = {}
    lowered_string = input_string.lower()
    #print(lowered_string)
    for s in lowered_string:
        if s in number_of_char:
            number_of_char[s] += 1
        else:
            number_of_char[s] = 1
    return number_of_char

def report(text_file):
    word_count = number_of_words(text_file)
    num_of_chars = number_of_characters(text_file)
    list_of_dict = []
    
    #def sort_on(dict):
        #for item in dict:
            #print(item)
        #return dict

    for key in num_of_chars:
        if key.isalpha():
            list_of_dict.append({key: num_of_chars[key]})
   
    sorted_list = sorted(list_of_dict, key=lambda x: list(x.values())[0], reverse=True)
    #print(list_of_dict.sort(reverse=True, key=lambda x: list(x.keys())[0]))
        
    
    print(sorted_list)
    
        
main()
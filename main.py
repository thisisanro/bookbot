def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_chars = count_characters(text)
    list_of_chars = list_from_dictionary(number_of_chars)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print("")
    print_report(list_of_chars)
    print("--- End report ---")

def print_report(list):
    for line in list:
        char = line['char']
        number = line['number']
        if char == ' ':
            char = "space"
        elif not char.isalpha():
            continue
        print(f"The {char} character was found {number} times")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return  f.read()
    
def count_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def list_from_dictionary(dict):
    result_list = []
    for k, v in dict.items():
        result_list.append({"char": k, "number": v})
    result_list.sort(reverse=True, key=sort_on)
    return result_list

def sort_on(dict):
    return dict["number"]
        
main()
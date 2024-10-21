def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_chars = count_characters(text)
    print(number_of_chars)

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
        
main()
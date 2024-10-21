def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(text)
    print(number_of_words)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return  f.read()
            
main()
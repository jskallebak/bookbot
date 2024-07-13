def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_characters(text)
    sorted = get_sorted(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for char in sorted:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_counter = {}
    for char in text:
        char = char.lower()
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter    

def get_sorted(dict):
    return sorted(dict.items(), key=lambda x:x[1], reverse=True)

def print_char_messages(a):
    for char in a:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

main()

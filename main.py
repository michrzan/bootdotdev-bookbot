import sys
from stats import get_num_words, count_chars_dict, char_dict_to_char_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dict):
    return dict["num"]

def print_book(filepath):
    book_text = get_book_text(filepath)
    d = count_chars_dict(book_text)
    l = char_dict_to_char_dicts(d)
    l.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    
    for line in l:
        print(f"{line["char"]}: {line["num"]}")
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_book(sys.argv[1])
        
main()

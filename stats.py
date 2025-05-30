from collections import defaultdict

def get_num_words(book_text):
    return len(book_text.split())
    
def count_chars_dict(book_text):   
    d = defaultdict(int)  # Initialize a defaultdict with int to count characters
    for char in book_text.lower():
        d[char] += 1
    return d
        
def char_dict_to_char_dicts(char_dict):
    return [{"char": char, "num": char_dict[char]} for char in sorted(char_dict) if char.isalpha()]        

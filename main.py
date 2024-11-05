def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        contents = get_text(f)
        word_count = get_word_count(contents)
        chars_dict = get_character_appearance(contents)
        report(book_path, word_count, chars_dict)
        

def get_text(book):
    return book.read()

def get_word_count(contents):
    words = contents.split()
    return len(words)

def get_character_appearance(contents):
    number_per_character = {}
    contents_lowered = contents.lower()
    contents_lowered_set = set(contents_lowered)
    for k in contents_lowered_set:
        v = 0
        for c in contents_lowered:
            if k == c:
                v += 1
        number_per_character[k] = v
    return number_per_character

#make dict sortable my making list of dict
def list_of_char_dict(chars_dict):
    list = []
    for k in chars_dict:
        v = chars_dict[k]
        new_entry = {"char": k, "num": v}
        list.append(new_entry)
    return list

def sort_key(list):
    return list["num"]

def report(book_path, word_count, chars_dict):
    print(f"--- Begin report on {book_path} ---")
    print(f"Words in the book: {word_count}\n")
    char_list = list_of_char_dict(chars_dict)
    char_list.sort(reverse=True, key=sort_key)
    for i in range(0, len(char_list), 1):
        if char_list[i]["char"].isalpha():
            print(f"The '{char_list[i]["char"]}' character was found {char_list[i]["num"]} times.")
    print("--- End Report ---")
    
main()
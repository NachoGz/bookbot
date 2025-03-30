
import os

# def count_words(text: str) -> int:
#     words = text.split()

#     return len(words)


# def count_characters(text: str) -> dict:
#     frequency = {}
#     for ch in text:
#         if ch.isalpha():
#             ch = ch.lower()
#             if ch not in frequency:
#                 frequency[ch] = 1
#             else:
#                 frequency[ch] += 1

#     return frequency


# def main():
#     books = os.listdir("books/")
#     book = input("What book would you like to analyze? (Use the name of the file in books/): ") + ".txt"
    
#     while book not in books:
#         print("Book not found... Try again!")
#         print()
#         book = input("What book would you like to analyze? (Use a name in books/): ") + ".txt"

#     with open(f"books/{book}") as f:
#         text = f.read()

#     amnt_words = count_words(text)

#     amnt_char = count_characters(text)

#     print(f"--- Begin report of books/{book} ---")
#     print(f"{amnt_words} words found in the document")
#     print()

#     for k,v in amnt_char.items():
#         print(f"The '{k}' character was found {v} times")

#     print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read()



if __name__ == '__main__':
    main()


    
    

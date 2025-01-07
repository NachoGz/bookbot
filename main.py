
import os

def count_words(text: str) -> int:
    words = text.split()

    return len(words)


def count_characters(text: str) -> dict:
    frequency = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1

    return frequency


def main():
    books = os.listdir("books/")
    book = input("What book would you like to analyze? (Use the name of the file in books/): ") + ".txt"
    
    while book not in books:
        print("Book not found... Try again!")
        print()
        book = input("What book would you like to analyze? (Use the name of the file in books/): ") + ".txt"

    with open(f"books/{book}") as f:
        text = f.read()

    amnt_words = count_words(text)

    amnt_char = count_characters(text)

    print(f"--- Begin report of books/{book} ---")
    print(f"{amnt_words} words found in the document")
    print()

    for k,v in amnt_char.items():
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")


if __name__ == '__main__':
    main()


    
    

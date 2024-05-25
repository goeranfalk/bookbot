def main():
    book = "books/frankenstein.txt"
    file_content = open_book(book)
    count = wordcount(file_content)
    letter = letter_count(file_content)

    print(f"--- Begin report of book {book} ---")
    print(f"{count} words found in the document")
    print()

    for key, value in letter.items():
        if not key.isalpha():
            continue
        print(f"The {key} character was found {value} times")

    print("--- End report ---")


def wordcount(content):
    word = content.split()
    return len(word)


def open_book(book):
    with open(book) as f:
        return f.read()


def letter_count(st):
    letter = {}
    for x in st:
        lowered = x.lower()
        if lowered in letter:
            letter[lowered] += 1
        else:
            letter[lowered] = 1
    return letter


if __name__ == "__main__":
    main()

import sys
from stats import get_num_words, letter_count, sort_on


def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    get_num_words(book_text)
    st = letter_count(book_text)
    sortert_liste = sort_on(st)

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sortert_liste:
        character = item["name"]
        count = item["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

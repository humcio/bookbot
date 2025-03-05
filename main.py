from stats import get_word_count, char_count, sort_dict
import sys

def main():
    path = sys.argv[1]
    num_words = get_word_count(path)
    count = char_count(path)
    sorted_count = sort_dict(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        print(f"{item}: {sorted_count[item]}")
    print("============= END ===============")
    #print(count)
    #print(sorted_count)


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
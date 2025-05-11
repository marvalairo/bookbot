from stats import get_num_words
from stats import count_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]
with open(path_to_file) as f:
    file_content = f.read()

word_count = get_num_words(file_content)
char_list = count_characters(file_content)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in char_list:
    print(f"{item['char']}: {item['num']}")
#print(char_counts)
print("============= END ===============")


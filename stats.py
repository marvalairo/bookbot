
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list




'''
path_to_file = 'books/frankenstein.txt'

# print(count_characters(path_to_file))


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
for vehicle in vehicles:
    print(f"name: {vehicle['name']}, num: {vehicle['num']}")
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
'''
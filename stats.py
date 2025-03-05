def get_word_count(path):
    file = open(path, "r")
    file_contents = file.read().split()
    return len(file_contents)
    
def char_count(path):
    file = open(path, "r")
    file_contents = file.read().lower()
    count = {}
    for char in file_contents:
        if char in count: #adds count to each letter
            count[char] += 1
        elif char == " " or char == "\n": #ignores whitespace
            pass
        else: #adds new entry if character is met for first time
            count[char] = 1
    return count

def sort_dict(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict
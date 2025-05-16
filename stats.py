"""
Counts the total number of words in a string,
if the string is massive it will ignore any major whitespaces

Args:
    text: The string to be counted

Returns:
    The count of words as a integer
"""
def get_num_words(text):
    count = len(text.split())
    return count

"""
Counts the number of times each character is in the argument string,
inclusive to symbols and spaces but excludes lower and upperclass characters

Args:
    text: The string to be counted

Returns:
    A dictionary of String -> Integer for each character counted
"""
def get_num_each_char(text):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

"""
A function that takes a dictionary and sorts it based on
variable from highest to lowest count

Args:
    dict: The dictionary to be sorted from highest to lowest

Returns:
    A dictionary that is sorted from highest to lowest
"""
def sort_dict(to_sort):
    sorted_dict = dict(sorted(to_sort.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
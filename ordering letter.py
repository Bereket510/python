
def order_alphabetically(strings):
    """
    Orders a list of strings alphabetically (case-insensitive).

    Args:
        strings: A list of strings.

    Returns:
        A new list of strings, sorted alphabetically.  Returns an empty
        list if the input is None or an empty list.
    """

    if strings is None or not strings:  # Handle empty or None input
        return []

    return sorted(strings, key=str.lower)  # Case-insensitive sort


# Example Usage:
words = ["zebra", "apple", "Cat", "banana", "Dog", "elephant"]
sorted_words = order_alphabetically(words)
print(sorted_words)  # Output: ['apple', 'banana', 'Cat', 'Dog', 'elephant', 'zebra']

# Example with numbers (will be sorted as strings):
mixed = ["zebra", "10", "apple", "2", "Cat"]
sorted_mixed = order_alphabetically(mixed)
print(sorted_mixed) # Output: ['10', '2', 'apple', 'Cat', 'zebra']

# Example with empty list:
empty_list = []
sorted_empty = order_alphabetically(empty_list)
print(sorted_empty) # Output: []

# Example with None:
none_list = None
sorted_none = order_alphabetically(none_list)
print(sorted_none) # Output: []


# More concise version (using lambda for the key):

def order_alphabetically_concise(strings):
    if strings is None or not strings:
        return []
    return sorted(strings, key=lambda s: s.lower())

words = ["zebra", "apple", "Cat", "banana", "Dog", "elephant"]
sorted_words = order_alphabetically_concise(words)
print(sorted_words)  # Output: ['apple', 'banana', 'Cat', 'Dog', 'elephant', 'zebra'
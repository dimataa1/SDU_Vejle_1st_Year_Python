"""
Task 3 - find_space(name) and make_username(name)

find_space(name): uses a linear search (loop + counter) to return
the index of the first space in name, or -1 if there is none.

make_username(name): turns 'Ada Lovelace' into 'alovelace'.
Handles the case where there is no whitespace by returning the
lowercased name.
"""

def find_space(name):
    """
    Performs a linear search for the first space character in name.

    name: the string to search
    Returns the index of the first space, or -1 if none is found.
    """
    index = 0
    for char in name:
        if char == " ":
            return index
        index += 1
    # loop finished without finding a space
    return -1


print(find_space("Ada Lovelace"))  # 3
print(find_space("Python"))        # -1


def make_username(name):
    """
    Builds a username from a full name: first letter of the first
    name (lowercased) + lowercased last name.

    name: a full name, e.g. 'Ada Lovelace'
    If there is no whitespace, returns the whole name lowercased.
    """
    space_index = find_space(name)

    if space_index == -1:
        # no space found, so there's no separate first/last name
        return name.lower()

    first_initial = name[0].lower()
    # the last name starts right after the space
    last_name = name[space_index + 1:].lower()

    return first_initial + last_name


print(make_username("Ada Lovelace"))  # alovelace
print(make_username("Python"))        # python
"""Module for funny string manipulations"""

def bubbleize(text):
    """Returns bubbleized string.
    """
    chars = []
    for idx, char in enumerate(text):
        if idx %2 :
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return"".join(chars)
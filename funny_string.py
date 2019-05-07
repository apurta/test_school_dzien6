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
    return "".join(chars)

#############################

from random import randint

def randomize(text):
    """Returns randomized string.
    Args:
        text: text to randomize
    Return:
        randomized text
    """
    chars = []
    for idx, char in enumerate(text):
        if randint (0, 1):
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return "".join(chars)

#################################


changes changes

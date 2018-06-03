

def is_palindrome(text):

    """Check id text is a palindrome.
    Args:
         text: string to be checked
    Returns:
        True if text is a palindrome, False otherwise
    """

    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text [len(text) -i-1]: # != a nie == bo fukcja przerwie się gdy znajdzie coś co nie pasuje
            return False
    return True

print(is_palindrome("oko"))
print(is_palindrome("Anna"))


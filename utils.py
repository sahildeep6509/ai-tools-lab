def is_palindrome(s):
    """
    Check whether a string is a palindrome.

    A palindrome is a word or phrase that reads the same forward and backward.
    Example: 'madam', 'racecar'
    """
    return s == s[::-1]


def count_words(text):
    """
    Count the number of words in a given text.

    Words are separated by spaces.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: (C * 9/5) + 32
    """
    return (c * 9/5) + 32


# Example usage
print(is_palindrome("madam"))
print(count_words("Hello world from AI lab"))
print(celsius_to_fahrenheit(25))
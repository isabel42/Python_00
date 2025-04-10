
"""
Text Properties Counter

This script counts various properties of the input text, including:
- Uppercase letters
- Lowercase letters
- Punctuation marks
- Spaces
- Digits

Usage:
    Run the script with an optional argument:
    $ python script_name.py "Your text here"
    
    If no argument is provided, you will be prompted to enter text.

Note:
    - The script handles multiple lines of text if input through the prompt.
    - It considers '...' as a special punctuation case and counts it accordingly.

Author: Isabel Tovar
Date: 10 April 2025
"""

import sys
def count_print(text, carriage_return):

    punctuation_marks = ['.', '?', '!', ',', ':',';', '-','—', '[', ']', '{', '}', '(', ')', "'", '"']

    count_marks = sum(text.count(mark) for mark in punctuation_marks) - 2 * text.count('...')
    count_upper = sum(1 for char in text if char.isupper())
    count_lower = sum(1 for char in text if char.islower())
    count_space = text.count(' ') + carriage_return
    count_digits = sum(1 for char in text if char.isdigit())

    print("The text contains", len(text) + carriage_return, "characters:")
    print(count_upper, "upper letters")
    print(count_lower, "lower letters")
    print(count_marks, "punctuation marks")
    print(count_space, "spaces")
    print(count_digits, "digits")


def main():

    carriage_return  = 0

    if len(sys.argv) <= 2:
        if len(sys.argv) == 1:
            print ("What is the text to count?")
            text = ""
            while text == "":
                carriage_return += 1
                text = input()
        else:
            text = sys.argv[1]

        count_print(text, carriage_return)

    else:
        print("AssertionError: more than one argument provided")


if __name__ == "__main__":
    # print(__doc__)
    main()
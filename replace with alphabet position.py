'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
(as a string)
'''
#Solution 1
def alphabet_position(text):
    from string import ascii_lowercase
    LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)

#Solution 2
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

#Solution 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')

'''
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is the first word,
     which is always capitalised.

Write a function that will convert a string into title case,
given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string --
it should behave in the same way even if the case of the minor word string is changed

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words
that must always be lowercase except for the first word in the string.

###Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
'''

#Nuaiman's Solution
def title_case(title, minor_words = ''):

    title = title.lower()
    New = title.title()
    Words = New.split()
    p = minor_words.lower()
    Minors = p.split()
    Arr = []
    for n in range(len(Words)):
        x = Words[n].lower()
        if x in Minors and n != 0:
            Arr.append(x)
        else:
            Arr.append(Words[n])
    string = " ".join(Arr)        
    return string

#Solution 2
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

#Solution 3
def title_case(title, minor_words=''):
    return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))

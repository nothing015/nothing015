'''

The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
#Nuaiman's Solution
def count(string):
    if string == "":
        return {}
    Alphabets = {}
    for c in string:
        if c not in Alphabets:
            Alphabets.update({c:1})
        else:
            Alphabets[c] += 1
    return Alphabets

#Solution 2
from collections import Counter

def count(string):
    return Counter(string)

#Solution 3
def count(string):
  
    return {i: string.count(i) for i in string}

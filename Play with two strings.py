'''
Input Strings a and b:
For every character in string a swap the casing of every
occurrence of the same character in string b.

Then do the same casing swap with the inputs reversed.
Return a single string consisting of the changed version
of a followed by the changed version of b.
A char of a is in b regardless if it's in upper or lower case - see the testcases too.
I think that's all;-)...

Some easy examples:

Input: "abc" and "cde"      => Output: "abCCde" 
Input: "ab" and "aba"       => Output: "aBABA"
Input: "abab" and "bababa"  => Output: "ABABbababa"
'''

#Nuaiman's Solution
def work_on_strings(a,b):
    temp1 = ""        # First part where a letters are checked with b
    temp2 = ""        # Second part where b letters are checked with a
    for c in a:
        if c.casefold() in b.casefold() and b.casefold().count(c.casefold())%2 != 0:      # Letters checked with lowercase only
            temp1 += c.swapcase()                      # Case swapped, NOT capitalized
        else:
            temp1 += c
            
    for l in b:
        if l.casefold() in a.casefold() and a.casefold().count(l.casefold())%2 != 0:
            temp2 += l.swapcase()
        else:
            temp2 += l
            
            
    return temp1+temp2        

#Solution 1
def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)

#Solution 2
from collections import Counter

def swap_them(a, b):
    cnt = Counter(b.lower())
    return "".join(c.swapcase() if cnt[c.lower()] % 2 else c for c in a)

def work_on_strings(a, b):
    return swap_them(a, b) + swap_them(b, a)

#Solution 3
from collections import Counter
import re

def swaper(m):       return m[0].swapcase()
def buildPattern(s): return f"[{ ''.join(c for c,n in Counter(s.lower()).items() if n&1) or ' ' }]"
def player(a,b):     return re.sub(buildPattern(b), swaper, a, flags=re.I)

def work_on_strings(a,b): return player(a,b)+player(b,a)






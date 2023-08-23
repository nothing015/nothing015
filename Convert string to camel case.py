'''
Complete the method/function so that it converts dash/underscore delimited words
into camel casing. The first word within the output should be capitalized only if the
original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

'''
#Nuaiman's Solution
def to_camel_case(text):
    if text.find('_') != -1:
        text = text.replace('_', '-')
    DashPresent = False
    for c in text:
        if c == '-':
            DashPresent = True
    Array = []        
    if DashPresent == True:
        Array = text.split('-')
    Finaltext = ''
    for e in range(len(Array)):
        if e == 0:
            Finaltext = Finaltext + Array[0]
        else:
            Finaltext = Finaltext + Array[e].capitalize()
    if text =='':
        Finaltext = ''
    return(Finaltext)

#Solution 1
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

#Solution 2
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

#Solution 3
import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)




'''
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"
'''

#Nuaiman's Solution
def spin_words(sentence):
    Array = sentence.split()
    ReturnValue = ""
    for n in Array:
        lenght = len(n)
        if lenght >= 5:
            NewWord = ""
            for m in range(lenght):
                NewWord = NewWord + n[lenght-1-m]
        else:
            NewWord = n
        ReturnValue = ReturnValue +" "+ NewWord    
    FinalValue = ReturnValue.lstrip()        
            
    return FinalValue

#Solution 1
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

#Solution 2
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

#Solution 3
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string




    

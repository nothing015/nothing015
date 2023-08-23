'''
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take
the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones
-- everytime you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a
single block for each letter (direction) and you know it takes you one minute
to traverse one city block, so create a function that will return true if the walk
the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.
'''

#Nuaiman's Solution
def is_valid_walk(walk):
    min = 0
    Verticaldistance = 0
    Horizontaldistance = 0
    flag = False
    count = 0
    if len(walk) == 10:
        for c in walk:
            if c == 'n':
                Verticaldistance += 1
            elif c == 's':
                Verticaldistance -= 1
            elif c == 'e':
                Horizontaldistance += 1
            elif c == 'w':
                Horizontaldistance -= 1
        if Verticaldistance == 0 and Horizontaldistance == 0:
            flag = True
            
    return flag

#Solution 1
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

#Solution 2
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False




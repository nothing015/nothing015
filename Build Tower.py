'''
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;

for example, a tower of 3 floors looks like below

[
                          '  *  ', 
                          ' *** ', 
                          '*****'
]
and a tower of 6 floors looks like below

[
                       '     *     ', 
                       '    ***    ', 
                       '   *****   ', 
                       '  *******  ', 
                       ' ********* ', 
                       '***********'
]

'''
#Nuaiman's Solution
def tower_builder(n_floors):
    tower = []
    count = 1
    index = 1
    for m in range((n_floors)-1):
        index = index + 2
    for n in range(n_floors):
        Astring = ""
        gapstring = ""
        string = ""
        for i in range(count):
            Astring = Astring + "*"
        for j in range((index - count)//2):
            gapstring = gapstring +" "
        string = gapstring + Astring + gapstring
        tower.append(string)
        count = count + 2
    return tower
while True:
    x = int(input("Enter the number of tower levels you want: "))
    y = iter(tower_builder(x))
    for n in range(x):
        print(next(y))

#Solution 1
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]    

#Solution 2
def tower_builder(n_floors):
    if n_floors == 0:
        return []
        
    count = 1
    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)
    
    return result

#Solution 3
def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]









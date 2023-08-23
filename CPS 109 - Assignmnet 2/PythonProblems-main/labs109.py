# Name: Mohammad Nuaiman Hasan
# ID: 501151286

# Problem 2
def is_ascending(items):
    if len(items) == 0 or len(items) == 1:
        return True
    else:
        flag = True
        for i in range(1, len(items)):
            if items[0] != items[1] and  items[0] < items[1]:
                if i != 0:
                    if items[i-1] < items[i]:
                        pass
                    else:
                        flag = False
                else:
                    pass
            else:
                flag = False
        return flag

# Problem 3
def riffle(items, out = True):

    lst1 = []
    lst2 = []
    for i in range(len(items)//2):
        lst1.append(items[i])
    for i in range(len(items)//2, len(items)):
        lst2.append(items[i])
    result = []
    if out:
        for n in range(len(items)//2):
            result.append(lst1[n])
            result.append(lst2[n])
    else:
        for n in range(len(items) // 2):
            result.append(lst2[n])
            result.append(lst1[n])
    return result

# Problem 4
def only_odd_digits(n):
    i = 0
    flag = True
    while i < len(str(n)):
        if int(str(n)[i])%2 == 0:
            flag = False
        i += 1
    return flag

# Problem 5
def is_cyclops(n):
    if len(str(n))%2 == 0:
        return False
    else:
        mid = len(str(n))//2
        if str(n)[mid] != '0':
            return False
        else:
            if '0' not in str(n)[:mid]:
                if '0' not in str(n)[mid+1:]:
                    return True
                else:
                    return False
            else:
                return False

# Problem 6
def domino_cycle(tiles):
    flag = True
    if tiles == []:
        return flag
    else:
        maxRow = len(tiles)
        if maxRow == 1:
            if tiles[0][0] == tiles[0][1]:
                return flag
            else:
                return False
        if tiles[0][0] == tiles[maxRow-1][1] and tiles[0][1] == tiles[1][0]:
            row = 0
            col = 0
            for r in range(maxRow):
                if (row == 0 and col == 0):
                    col += 1
                else:
                    if col == 0:
                        if tiles[row][col] != tiles[row-1][col+1]:
                            flag = False
                        col += 1
                    if col == 1:
                        if tiles[row][col] != tiles[row+1][col-1]:
                            flag = False
                        col = 0
                        row += 1
            if tiles[maxRow-2][1] != tiles[maxRow-1][0]:
                flag = False
        else:
            flag = False
    return flag

# Problem 7
def colour_trio(colours):
    lst = ['r', 'y', 'b']
    if len(colours) == 1:
        return colours
    elif len(colours) == 2:
        if colours[0] == colours[1]:
            return colours[0]
        else:
            for c in lst:
                if c not in colours:
                    return c
    elif len(colours) >= 3:
        string = ''
        while len(colours) != 1:
            string = ''
            for c in range(len(colours)):
                if c != len(colours) - 1:
                    if colours[c] == colours[c+1]:
                        string += colours[c]
                    else:
                        for e in lst:
                            if e != colours[c] and e != colours[c+1]:
                                string += e
            colours = string
        return colours

# Problem 9
def extract_increasing(digits):
    if digits == '':
        return []
    result = [int(digits[0])]
    i = 0
    key = int(digits[0])
    while 1 < len(digits): #and i < len(digits):
        if len(digits) > 1:
            num = int(digits[1])
            j = 2
            c = 1
            if num <= key:
                while num <= key and j < len(digits):
                    num = int(str(num) + str(digits[j]))
                    j += 1
                    c += 1

            if num > key:
                key = num
                result.append((num))
            digits = digits[c:]
            num = 0

        i += 1
    return result

# Problem 10
def safe_squares_rooks(n, rooks):
    lst = [[i,j] for i in range(n) for j in range(n)]
    for rook in rooks:
        for i in lst:
            if i[0] == rook[0]:
                i[0] = ''
            if i[1] == rook[1]:
                i[1] = ''
    safe = 0
    for square in lst:
        if not '' in square:
            safe += 1
    return safe

# Problem 23
def count_growlers(animals):
    growling = 0
    for a in range(len(animals)):
        animal = animals[a]
        if animals[a] == 'cat' or animals[a] == 'dog':
            if a != 0:
                i = a - 1
                cats = 0
                dogs = 0
                while i >= 0:
                    if animals[i] == 'cat' or animals[i] == 'tac':
                        cats += 1
                    else:
                        dogs += 1
                    i -= 1
                if dogs > cats:
                    growling += 1
        else:
            if a != len(animals)-1:
                i = a + 1
                cats = 0
                dogs = 0
                while i < len(animals):
                    if animals[i] == 'cat' or animals[i] == 'tac':
                        cats += 1
                    else:
                        dogs += 1
                    i += 1
                if dogs > cats:
                    growling += 1

    return growling

    return growling

# Problem 32
def three_summers(items, goal, j = None, i = 0):
    j = len(items) - 1 if j is None else j
    for g in range(len(items)):
        toAdd = items[g]
        i = 0
        j = len(items) - 1
        while i<j and (items[i] != items[g] and items[j] != items[g]):
            x = items[i] +items[j]+items[g]
            if x == goal:
                return True
            elif x < goal:
                i += 1
            else:
                j -= 1
    return False

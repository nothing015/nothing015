'''
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''
#Nuaiman's solution
def digital_root(n):
    lenght = len(str(n))
    total = 0
    num = str(n)
    for i in range(lenght):
        total = total + int(num[i])
    if total > 9:
        flag = False
        while flag == False:
            lenght = len(str(total))
            num = str(total)
            total = 0
            for j in range(lenght):
                total = total + int(num[j])
            if total < 10:
                    flag = True
    return total

#solution 1
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

#solution 2
def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root

#solution 3
def digital_root(n):
    return n%9 or n and 9



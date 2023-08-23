'''
Write a function, persistence, that takes in a positive parameter num
and returns its multiplicative persistence, which is the number of times
you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39)     # returns 3, because 3*9=27, 2*7=14, 1*4=4
                               # and 4 has only one digit
                  
 persistence(999)   # returns 4, because 9*9*9=729, 7*2*9=126,
                               # 1*2*6=12, and finally 1*2=2

 persistence(4)      # returns 0, because 4 is already a one-digit number

'''

#Nuaiman's Solution
def persistence(num):
    flag = False
    count = 0
    while flag == False:
        if num < 9:
            return count
            flag = True
        else:
            count += 1
            OldNum = str(num)
            num = 1
            for j in OldNum:
                num *= int(j)

#Solution 1
import operator

def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

#Solution 2
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

#Solution 3
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

#Solution 4
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1



















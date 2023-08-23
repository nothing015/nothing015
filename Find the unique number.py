'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
'''
#Nuaiman's Solution
def find_uniq(arr):
    #check for first element
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    else:
        #check for the rest of the array
        for e in range(len(arr)):
            if arr[0] != arr[e]:
                return arr[e]

#Solution 1
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

#Solution 2
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e

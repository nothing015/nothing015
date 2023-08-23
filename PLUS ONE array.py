'''

Given an array of integers of any length, return an array that has 1 added to the value
represented by the array.

** The array can't be empty
** Only non-negative, single digit integers are allowed
** Return nil (or your language's equivalent) for invalid inputs.

Examples
The array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
[4, 3, 2, 5] would return [4, 3, 2, 6]
'''

#Nuaiman's Solution
def up_array(arr):
    if arr is None:
        return None
    string = ""
    NewNum = 0
    for i in range(len(arr)):
        if arr[i] < 0 or arr[i] > 9:
            return None
        else:
            string = string + str(arr[i])
    if string != "":
        NewNum = str(int(string) + 1)
    if NewNum == 0:
        return None
    NewArr = []
    for c in str(NewNum):
        NewArr.append(int(c))           
    return NewArr

#Solution 1
def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]

#Solution 2
def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]

#Solution 3
def up_array(arr):
    if arr and all(0<=v<=9 for v in arr):
        return map(int, str(int(''.join(map(str,arr)))+1))









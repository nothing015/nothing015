'''
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


'''

#Nuaiman's Solution
def move_zeros(array):
    if array == "":
        return array
    zeroes = array.count(0)
    for n in range(zeroes):
        array.remove(0)
    for m in range(zeroes):
        array.append(0)
    return array

#Solution 1
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

#Solution 2
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)




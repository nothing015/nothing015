'''
Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

'''
#Nuaiman's Solution
def array_diff(a, b):
    diff = []
    for r in range(len(a)):
        if a[r] not in b:
            diff.append(a[r])
    return diff

#Solution 2
def array_diff(a, b):
    return [x for x in a if x not in b]

#Solution 3
def array_diff(a, b):
    return [x for x in a if x not in set(b)]


#Solution 4
def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]

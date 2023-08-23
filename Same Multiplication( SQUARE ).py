'''

Given two arrays a and b write a function comp(a, b) that checks whether
the two arrays have the "same" elements, with the same multiplicities.
"Same" means, here, that the elements in b are the elements in a squared,
regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, Elixir, Haskell, PureScript, Pascal, R, Rust, Shell).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
'''

#Nuaiman's Solution
def comp(a, b):
    square = 0
    Flag = True
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False
    for e in range(len(a)):
        square = a[e]*a[e]
        if b.count(square) == 0:
            Flag = False
        else:
            b.pop(b.index(square))

    return Flag

#Solution 2
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

#Solution 3
def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []

#Solution 3
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

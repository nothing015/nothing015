'''
Bob is preparing to pass IQ test. The most frequent task in this test
is to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among
the given numbers finds one that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
'''

#Nuaiman's Solution
def iq_test(numbers):
    odds = 0
    evens = 0
    num = numbers.split(" ")
    for n in range(len(num)):
        if int(num[n]) % 2 != 0:
            odds = odds + 1
            oddplace = n + 1
        elif int(num[n]) % 2 == 0:
            evens = evens + 1
            evenplace = n + 1
    if odds == 1:
        return oddplace
    elif evens == 1:
        return evenplace

#Solution 1
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

#Solution 2
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1

#Solution 3
def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    return eo.index(1 if eo.count(0)>1 else 0)+1






















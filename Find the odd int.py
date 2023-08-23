'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''

#Solution 1
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

#Solution 2
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

#Solution 3
import operator

def find_it(xs):
    return reduce(operator.xor, xs)

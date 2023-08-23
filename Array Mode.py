'''

Complete the method which returns the number which is most frequent in the given input array.
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
'''

#Nuaiman's Solution
def highest_rank(arr):
    count = []
    modes = []
    for n in range(len(arr)):
        count.append(arr.count(arr[n]))
    for m in range(len(count)):
        if count[m] == max(count):
            modes.append(arr[m])
    return max(modes)

#Solution 2
from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)

#Solution 3
def highest_rank(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]

#Solution 4
def highest_rank(arr):
    return max(sorted(arr,reverse=True), key=arr.count)

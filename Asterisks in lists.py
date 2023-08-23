'''
Let's assume that we want to assign the first element
of list/tuple/set to aand remaining elements to b.
In general, we will accomplish this using slicing.
'''
## general approach
nums = [i for i in range(1, 6)]
a = nums[0]
b = nums[1:]
print(a, b)    #prints: 1 [2, 3, 4, 5]

#Now, we are going to use the * operator to implement this in a single line of code.
nums = [i for i in range(1, 6)]

## a will be 1 and b will be a list containing remaining elements
a, *b = nums
print(a, b)    #prints: 1 [2, 3, 4, 5]

print(*nums)
print(nums)

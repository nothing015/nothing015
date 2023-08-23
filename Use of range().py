'''
In simple terms, range() allows user to generate a series of numbers within a given range.
Depending on how many arguments user is passing to the function,
user can decide where that series of numbers will begin and end


start: integer starting from which the sequence of integers is to be returned
stop: integer before which the sequence of integers is to be returned.
        The range of integers end at stop – 1.
step: integer value which determines the increment between each integer in the sequence

'''
  
# printing a number
for i in range(10):
    print(i, end =" ")
print()                        # prints 0 1 2 3 4 5 6 7 8 9 
  
# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end =" ")
print()                        # prints 10 20 30 40 
  
# performing sum of natural number
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)        # prints Sum of first 10 natural number : 55

# Python program to print whole number using range()
  
# printing first 10 whole number
for i in range(10):
    print(i, end =" ")
print()                         # 0 1 2 3 4 5 6 7 8 9 
  
# printing first 20 whole number
for i in range(20):
    print(i, end = " ")    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

# Python program to print natural number using range
  
# printing a natural number upto 20
for i in range(1, 20):
    print(i, end =" ")
print()                         # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
  
# printing a natural number from 5 t0 20
for i in range(5, 20):
    print(i, end =" ")     # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 

# Python program to print all number divisible by 3 and 5
   
# using range to print number divisible by 3
for i in range(0, 30, 3):
    print(i, end = " ")
print()
  
# using range to print number divisible by 5
for  i in range(0, 50, 5):
     print(i, end = " ")
     
# Python program to concatenate the result of two range functions
  
  
from itertools import chain
  
  
# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))
  
for i in res:
    print(i, end=" ")      #Concatenating the result
                                  # 0 1 2 3 4 10 12 14 16 18
                                  
# Python program to demonstrate range function
  
ele = range(10)[0]
print("First element:", ele)
  
ele = range(10)[-1]
print("\nLast element:", ele)   
  
ele = range(10)[4]
print("\nFifth element:", ele)

#Outputs:
#First element: 0

#Last element: 9

#Fifth element: 4

'''
range() function only works with the integers i.e. whole numbers.
All argument must be integers.

User can not pass a string or float number or any other type in a start,
stop and step argument of a range().

All three arguments can be positive or negative.

The step value must not be zero. If a step is zero python raises a ValueError exception.

In Python, range() is a type

User can access items in a range() by index, just as user do with a list

'''




















    


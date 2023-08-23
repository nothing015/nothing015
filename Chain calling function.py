'''
Chain function calling
We want to create a function that will add numbers together when called in succession.

add(1)(2);
// returns 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3); // 6
add(1)(2)(3)(4); // 10
add(1)(2)(3)(4)(5); // 15
and so on.

A single call should return the number passed in.

add(1); // 1
We should be able to store the returned values and reuse them.

var addTwo = add(2);
addTwo; // 2
addTwo + 5; // 7
addTwo(3); // 5
addTwo(3)(5); // 10
We can assume any number being passed in will be valid whole number.
'''
#Nuaiman's Solution with assistance
class add(int):
    def __call__(self, v):
        return add(self + v)

#Solution 2
class add(int):
    __call__ = lambda self, value: add(self + value)

#Solution 3
def add(n):
    return MyInt(n)
    
class MyInt(object):
    def __init__(self, n):
        self.value = n

    def __add__(self, n):
        return MyInt(self.value + n)
        
    def __sub__(self, n):
        return MyInt(self.value - n)
        
    def __call__(self, n):
        return MyInt(self.value + n)
        
    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        else:
            return self.value == other





        


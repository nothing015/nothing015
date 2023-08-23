'''

This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, dividedBy 
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner
function represents the right operand

Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

'''

#Solution 1
class Int(int):
    #Pseudo-int with operation on it.
    def __init__(self, value=0):
        super(Int, self).__init__(value)
        self.operation = None

    def __call__(self, operand=None):
        if operand is None:
            return self
        elif operand.operation == 'times':
            return self * operand
        elif operand.operation == 'plus':
            return self + operand
        elif operand.operation == 'minus':
            return self - operand
        elif operand.operation == 'divided_by':
            return self / operand


def operation(name):
    def _operation(arg):
        arg.operation = name
        return arg
    return _operation


(zero, one, two, three, four, five, six, seven, eight, nine) = (
                                        Int(0),Int(1), Int(2), Int(3), Int(4),
                                        Int(5), Int(6), Int(7), Int(8), Int(9))

plus = operation('plus')
minus = operation('minus')
times = operation('times')
divided_by = operation('divided_by')

#Solution 2
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

#Solution 3
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x//y







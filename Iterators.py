
'''
Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you can get an iterator from.
'''

#as a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# as a string
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('Nuaiman, \n Hasan \n Mohammad')
print(' Hasan Mohammad, \t \t Nuaiman')

'''
The __iter__() method acts similar, you can do operations (initializing etc.),
but must always return the iterator object itself

The __next__() method also allows you to do operations,
and must return the next item in the sequence.
'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
In the __next__() method, we can add a terminating condition
to raise an error if the iteration is done a specified number of times:
'''
class MyNumbers:   #The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

'''
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.

'''
#as a dictioanary
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

#as a tuple
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)










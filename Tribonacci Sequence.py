'''
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature),
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]

But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically
shifts the common Fibonacci sequence by once place, you may be tempted to think that we would
get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function
that given a signature array/list, returns the first n elements - signature included of the so
seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number;
if n == 0, then return an empty array (except in C return NULL) and be ready for
anything else which is not clearly specified ;)

'''
#Nuaiman's Solution
def tribonacci(signature, n):
    array = []
    #checking for n individually
    if n == 0:
        return array
    if n == 1:
        array.append(signature[0])
        return array
    if n == 2:
        array.append(signature[0])
        array.append(signature[1])
        return array
    if len(signature) == len(array):
        array = signature
        return array
    #chekhing for n greater than 3 as array differs(does not ahve the same trend)
    else:
        array.append(signature[0])
        array.append(signature[1])
        array.append(signature[2])
        
    for num in range(3, n):
        array.append(array[num-1]+array[num-2]+array[num-3])
        
    return array    
        
#Solution 1
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

#Solution 2
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]















    



  



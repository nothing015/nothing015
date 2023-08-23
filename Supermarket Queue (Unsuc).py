'''
There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they require to check out.

n: a positive integer, the number of checkout tills.

OUTPUT
The function should return an integer, the total time required.
'''

#Solution 1
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

#Solution 2
import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

#Solution 3
def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)

#Solution 4
def queue_time(customers, n):
    queues = [0] * n
    for i in customers:
        queues.sort()
        queues[0] += i
    return max(queues)




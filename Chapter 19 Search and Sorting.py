array = [120, 123, 124, 127, 129, 132, 134, 139, 145, 155, 159, 160]
upperbound = len(array) 
lowerbound = 0


def BinarySearch(array, upperbound, lowerbound, searchitem):
    if lowerbound <= upperbound:
        mid = (lowerbound + upperbound)//2
        if array[mid] == searchitem:
            return mid
        elif array[mid] < searchitem:
            return BinarySearch(array, upperbound, mid + 1, searchitem)
        elif array[mid] > searchitem:
            return BinarySearch(array, mid -1, lowerbound, searchitem)
    else:
        return -1

def BubbleSort(array):                               # Sorted by comparing each adjacent element
    flag = True
    n = len(array)
    while flag == True or n > 0:                    # Sorting the array backwards [...(3), (2), (1)]
        flag = False
        for count in range(n -1):                     # (n - 1) because the other part of the array is already sorted
            if array[count] > array[count+1]:    # Swapping according to the criteria
                temp = array[count]
                array[count] = array[count+1]
                array[count+1] = temp
        n = n - 1                                             # Decrementing the count to move backwards in the array
        
def InsertionSort(array):                                       # Sorted by moving elements approximately to the right place
    for n in range(1, len(array)):
        main = array[n]
        index = n-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        
        while index >= 0 and array[index] > main:
            array[index+1] = array[index]
            index -= 1
        array[index + 1] = main    

'''
Performance of a sorting routine may depend on the
initial order of the data and the number of data items.

The insertion sort performs better on partially sorted lists because,
when each element is found to be in the wrong order in the list, it is moved
to approximately the right place in the list. The bubble sort will only swap the
element in the wrong order with its neighbour.

As the number of elements in a list increases, the time taken to sort the list
increases. It has been shown that, as the number of elements increases, the
performance of the bubble sort deteriorates faster than the insertion sort.

'''

while True:
    searchitem = int(input("Enter the item you wanna search: "))
    x = BinarySearch(array, upperbound, lowerbound, searchitem)
    if x == -1:
        print("Item not found")
    else:
        print("Item found at index: "+ str(x+1))
    y = int(input("Do you want to sort anything in an ascending order? Enter 1 for YES or anything else for NO: "))
    if y == 1:
        arr = []
        n = int(input("Enter the length of your array: "))
        for m in range(n):
            arr.append(input("Enter the number you wanna add: "))
        InsertionSort(arr)
        print(arr)
            
            
     
        

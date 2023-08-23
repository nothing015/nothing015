
'''
class Node:
    def __init__(self, data = None, pointer = None):
        self.data = data
        self.ptr = pointer

class LinkedList:
    def __init__(self, Startpointer = None, Freepointer = 0):
        self.head = Startpointer
        self.free = Freepointer
        
    def InitialiseList(self, n, arr = []):
        for i in range(n-2):
            arr.append(Node(None, i + 1))
        arr.append(Node(None, -1))
        return arr

    def Insert(self, NewItem):
        if self.free != -1:
            NewP = self.free
            arr[NewP].data = NewItem
            self.free = arr(self.free).ptr
            CurrP = self.head
            PreviousP = -1
            
            while CurrP != -1 and arr[CurrP].data.casefold() < NewItem.casefold():
                PreviousP = CurrP
                CurrP = arr[CurrP].ptr

            if PreviousP == self.head:
                arr[NewP].ptr = self.head
                self.head = NewP
            else:
                arr(NewP).ptr = arr[PreviousP].ptr
                arr[PreviousP].ptr = NewP
                
    def PrintAlpha(self):
        nodeP = self.head
        while nodeP != -1:
            print(arr[node].data)
            nodeP = arr[node].pointer 



G = LinkedList().InitialiseList(7).PrintAlpha()'''

class treeNode:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data
        
class Tree:
    def __init__(self):
        self.root = -1
        self.free = 0
        self.array = []

    def Initialise(self, n):
        for i in range(int(n)-1):
            self.array.append(treeNode('', '', ''))
        self.array.append(treeNode(-1, '', ''))
        
    def insert(self, data):
       if self.array[0]:
           if data < self.array[0].data:
               if self.array[0].left is None:
                   self.array[0].left = treeNode('', '', data)
               else:
                    self.array[0].left.insert(data)
           elif data > self.array[0].data:
                if self.array[0].right is None:
                    self.array[0].right = treeNode('', '', data)
                else:
                    self.array[0].right.insert(data)
       else:
            self.array[0].data = data
         
    def PrintTree(self):
      if self.array[0].left:
         self.array[0].left.PrintTree()
      print( self.data),
      if self.array[0].right:
         self.array[0].right.PrintTree()    

x = Tree().Initialise(5).PrintTree()



































            



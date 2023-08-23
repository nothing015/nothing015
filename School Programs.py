##LINKED LIST
class ListNode:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer
						
def InitialiseList():
    global head
    global FreeP
    global NullP
    NullP = -1
    head = NullP
    FreeP = 0
    global Array
    Array = []
    for r in range (5):
        Array.append(ListNode(" ", r+1))		
    Array.append(ListNode(" ",NullP))

def InsertNode (NewItem):
    global head
    global FreeP
    global NullP
    NewP = FreeP
    Array[NewP].Data = NewItem       # Only place where data is being added, the rest works with pointers only
    FreeP= Array[FreeP].Pointer
	
    ThisP = head
    PrevP = NullP
    while ThisP != NullP and Array[ThisP].Data.casefold() < NewItem.casefold():    # Second condition not needed in case the NewItem can be inserted into any order
        PrevP = ThisP                          # Think of a dragon bridge(/\/\/\/\/\/\/\/\/\/) by making the current pointer into the previous pointer
        ThisP= Array[ThisP].Pointer    # Pointers are getting adjusted one by one
  
    if PrevP == NullP:                        # If only one node exists after insertion
        Array[NewP].Pointer = head
        head = NewP
    else:
        Array[NewP].Pointer = Array[PrevP].Pointer          # Giving NewItem's pointer the value of Previous item's pointer and giving the location of NewItem to Previous Item's pointer
        Array[PrevP].Pointer = NewP                                 # This step is mandatory, regardless of being a sorted linked list

def PrintAlpha():
    node = head
    while node != -1:
        print (Array[node].Data)
        node = Array[node].Pointer

def SearchItem(SItem):
    ThisP = head
    while ThisP != NullP and Array[ThisP].Data != SItem:
        ThisP = Array[ThisP].Pointer
    return ThisP

def DeleteItem(DItem):
    global head
    global FreeP
    global NullP
    ThisP = head
    while ThisP != NullP and Array[ThisP].Data != DItem:
        PrevP = ThisP
        ThisP = Array[ThisP].Pointer
    if ThisP != NullP:
        if ThisP == head:
            head = Array[head].Pointer
        else:
            Array[PrevP].Pointer = Array[ThisP].Pointer
        Array[ThisP].Pointer = FreeP
        FreeP = ThisP
        return True
    else:
        return False
        
##BINARY TREE
class TreeNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = TreeNode(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = TreeNode(data)
            else:
               self.right.insert(data)
      else:
         self.data = data    #Inserted at root node
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
    
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res

print("Options:\n"
      "1.Linked Lists \n"
      "2.Binary Tree \n"
      "3.End Program \n")

Order = 0
while Order != 3:
    Order = int(input("Please enter your command: "))
    if Order != 1 or Order != 2 or Order != 3:
        print("Invalid command.")
    if Order == 1:
        print ("Options: \n"
       "1. Initialise List \n"
       "2. Add Item \n"
       "3. Delete Item \n"
       "4. Search Item \n"
       "5. Print List as Table \n"
       "6. Print Items in Order \n"
       "7. End Program")
        Order = 0
        while Order != 7:
            Order = int(input("Please enter your command: "))
            if Order != 7:
                if Order == 1:
                    InitialiseList()
                    print ("List has been initialised.")
                if Order == 2:
                    InsertNode(input("Please type item to add: "))
                    print("Item has been added")
                if Order == 3:
                    status = DeleteItem(input("Enter Item to delete: "))
                    if status == True:
                        print("Item has been deleted.")
                    else:
                        print("Item not found.")
                if Order == 4:
                    node = SearchItem(input("Enter Item to search: "))
                    if node != -1:
                        print ("Item has been found in node ", node, "." )
                    else:
                        print ("Item not found.")
                    
                if Order == 5:
                    print ("Index     Data     Pointer")
                    for r in range(6):
                        print ("  ",r, "      ",Array[r].Data,"     ",Array[r].Pointer)
                if Order == 6:
                    PrintAlpha()
            else:
                print ("Session has ended.")
    if Order == 2:
        print ("Options: \n"
       "1. Insert Item Into Binary Tree \n"
       "2. Print The Binary Tree \n"
       "3. Traverse The Binary Tree In Order \n"
       "4. Traverse The Binary Tree Pre Oder \n"
       "5. End Program \n"
       "To Initialise The Tree, Please Exit and Restart the Program \n"
       "Before anything, please start with entering the root of the tree!!")
        Order = 0
        root = TreeNode(input("Please enter the root of the tree: ")+ "  #root")
        while Order != 5:
            Order = int(input("Please enter your command: "))
            if Order != 5:
                if Order == 1:
                    root.insert(input("Please enter a node you want to add: "))
                    print("A node has been added")
                  
                if Order == 2:
                    print(root.PrintTree())
                   
                if Order == 3:
                    print("Here is the tree in order \n")
                    print(root.inorderTraversal(root))
                    
                if Order == 4:
                    print("Here is the tree pre order \n")
                    print(root.PreorderTraversal(root))
                    
            else:
                print("Session has ended")
    else:
        print("Thank you for using the program.")
        





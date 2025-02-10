#LAB 3
#2023-EE-165
#WALEED AKRAM

#3.7 AddLast with resizing
import array as arr

class AList:
    def __init__(self):
        self.capacity = 10  # Start with a smaller initial capacity for testing
        self.item = arr.array('i', [0 for x in range(self.capacity)])
        self.current_size = 0

    def Resize(self):
        self.capacity *= 2
        p = arr.array('i', [0 for x in range(self.capacity)])  #step1:Create a new array with the new capacity
        for z in range(self.current_size): #step2:Copy elements to the new array
            p[z] = self.item[z]  
        self.item = p  #step3:Point to the new array

    def AddLast(self, i):
        if self.current_size == self.capacity:
            self.Resize()
            

        self.item[self.current_size] = i # Add the new item
        self.current_size += 1  # Increment the size

    def PrintList(self):
        return ' '.join(str(self.item[i]) for i in range(self.current_size))


    def GetLast(self):
        if self.current_size == 0:
            raise IndexError("Empty List")
        else:
            return self.item[self.current_size-1] #-1 bcz indexing starts from 0 in python

    def Get(self , i):
        if i<0 or i>self.current_size-1:
            print("Index is Out of Range")  #raise IndexError("Index is out of Range")
        else:
            return self.item[i]

    def size(self):
        return self.current_size
    
    def RemoveLast(self):
        if self.current_size == 0:
            print("Array is empty")
        else:
            self.item[self.current_size-1] = 0
            self.current_size -= 1
        


# Adding some initial elements
a = AList()
a.AddLast(5)
a.AddLast(10)
a.AddLast(15)
a.AddLast(20)

#a.PrintList()  # This will print the current elements in the array

#last = a.GetLast()
#print("The Last Element is: ", last)

#print("Element at index 1:", a.Get(1))  
#print("Element at index 4:", a.Get(4))
#print("Element at index 3:", a.Get(3)) 

#print("Current size of array is: " , a.size())

print("List before removal of last element: " ,a.PrintList())
print("Size of array before removal: " , a.size() )
print()

a.RemoveLast()  #we call removelast method
print("List after removal of last element: " ,a.PrintList())
print("Size of array after removal: " , a.size() )


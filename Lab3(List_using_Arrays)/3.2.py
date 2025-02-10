#LAB 3
#2023-EE-165
#WALEED AKRAM

#3.2 AddLast
import array as arr

class AList:
    def __init__(self):
        self.capacity = 10  # Start with a smaller initial capacity for testing
        self.item = arr.array('i', [0 for x in range(self.capacity)])
        self.current_size = 0

    def AddLast(self, i):
        if self.current_size == self.capacity:
            # Double the capacity
            self.capacity *= 2
            p = arr.array('i', [0 for x in range(self.capacity)])  #step1:Create a new array with the new capacity
            for z in range(self.current_size): #step2:Copy elements to the new array
                p[z] = self.item[z]  
            self.item = p  #step3:Point to the new array

        self.item[self.current_size] = i # Add the new item
        self.current_size += 1  # Increment the size

    def PrintList(self):
        for i in range(self.current_size):
            print(self.item[i], end=' ')
        print()

# Adding some initial elements
a = AList()
a.AddLast(5)
a.AddLast(10)
a.AddLast(15)
a.AddLast(20)

a.PrintList()  # This will print the current elements in the array



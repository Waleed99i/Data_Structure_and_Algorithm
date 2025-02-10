# LAB 3
# 2023-EE-165
# WALEED AKRAM

# 3.8 effective resize() for both removelast() and addlast()
import array as arr

class AList:
    def __init__(self):
        self.capacity = 10  # Start with a smaller initial capacity for testing
        self.item = arr.array('i', [0 for _ in range(self.capacity)])
        self.current_size = 0

    def Resize(self, new_capacity):
        # Create a new array with the specified new capacity
        p = arr.array('i', [0 for x in range(new_capacity)])  # Step 1: Create a new array with the new capacity
        for z in range(self.current_size):  # Step 2: Copy elements to the new array
            p[z] = self.item[z]
        self.item = p  # Step 3: Point to the new array
        self.capacity = new_capacity  # Update the capacity

    def AddLast(self, i):
        if self.current_size == self.capacity:
            self.Resize(self.capacity * 2)  # Double the capacity

        self.item[self.current_size] = i  # Add the new item
        self.current_size += 1  # Increment the size

    def PrintList(self):
        return ' '.join(str(self.item[i]) for i in range(self.current_size))

    def GetLast(self):
        if self.current_size == 0:
            raise IndexError("Empty List")
        else:
            return self.item[self.current_size - 1]  # -1 because indexing starts from 0 in Python

    def Get(self, i):
        if i < 0 or i >= self.current_size:  # Changed to >= for proper bounds checking
            print("Index is Out of Range")  # You could also raise an exception here
        else:
            return self.item[i]

    def size(self):
        return self.current_size
    
    def RemoveLast(self):
        if self.current_size == 0:
            print("Array is empty")
        else:
            self.item[self.current_size - 1] = 0  # Set the last element to zero
            self.current_size -= 1  # Decrement the size
            
            # Check if the current size is less than 25% of the capacity
            if self.current_size < self.capacity * 0.25 and self.capacity > 10:  # Ensure we don't shrink below initial capacity
                self.Resize(self.capacity // 2)  # Halve the capacity #smaller array

# Adding some initial elements
a = AList()
a.AddLast(5)
a.AddLast(10)
a.AddLast(15)
a.AddLast(20)

# Print the list and size before removal
print("List before removal of last element: ", a.PrintList())
print("Size of array before removal: ", a.size())
print()

a.RemoveLast()  # Call RemoveLast method
print("List after removal of last element: ", a.PrintList())
print("Size of array after removal: ", a.size())
#2023-EE-165
# Priority Queue

class PQ:
    def __init__(self):
        self.L = []
        self.i = 0

    def getParentOf(self, i):
        return int((i - 1) / 2)
    
    def swimUp(self):
        new_item_index = self.i
        parent_index = PQ.getParentOf(self, new_item_index)

        while new_item_index > 0 and self.L[parent_index] > self.L[new_item_index]:
            (self.L[new_item_index], self.L[parent_index]) = (self.L[parent_index], self.L[new_item_index])
            new_item_index = parent_index
            parent_index = PQ.getParentOf(self, new_item_index)

    def insert(self , k):
        self.L.append(k)
        #since already swimUp mai condition(while) lgai hui ha so ab yaha nhi aye gi
        PQ.swimUp(self)
        self.i += 1

    def peek(self):
        return self.L[0]
    
    def getLeftOf(self, i):
        return (2 * i + 1)
    
    def getRightOf(self, i):
        return (2 * i + 2)
    
    def Min(self, i1, i2):
        if self.L[i1] < self.L[i2]:
            return i1
        else:
            return i2

    def swimDown(self):
        new_item_index = 0  # Start from root
        left_index = PQ.getLeftOf(self, new_item_index)
        right_index = PQ.getRightOf(self, new_item_index)

        while left_index < len(self.L):  # Check if left child exists
            # Determine the minimum index among the current node and its children
            minimum = new_item_index
            
            if left_index < len(self.L) and self.L[left_index] < self.L[minimum]:
                minimum = left_index
            
            if right_index < len(self.L) and self.L[right_index] < self.L[minimum]:
                minimum = right_index

            # If the current node is less than or equal to the minimum child, we are done
            if minimum == new_item_index:
                break

            # Swap the current node with the minimum child
            (self.L[new_item_index], self.L[minimum]) = (self.L[minimum], self.L[new_item_index])
            
            # Move down to the minimum child
            new_item_index = minimum
            left_index = PQ.getLeftOf(self, new_item_index)
            right_index = PQ.getRightOf(self, new_item_index)

    def poll(self):
        p = self.L[0]
        # len(self.L)-1 is the Right most(last) index of the list
        (self.L[0], self.L[len(self.L)-1]) = (self.L[len(self.L)-1], self.L[0])
        self.L.pop() #remove/detatch
        PQ.swimDown(self)
        return p
        

p = PQ()
for k in [9,8,3,7,4]:
    p.insert(k)
print(p.L)
print(p.peek())
print(p.poll())
print(p.L)


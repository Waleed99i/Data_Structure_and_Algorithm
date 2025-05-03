
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
    
   
p = PQ()
for k in [1,5,7,0]:
    p.insert(k)
print(p.L)
print(p.peek())

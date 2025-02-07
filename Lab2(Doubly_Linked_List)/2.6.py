#LAB2
#2023-EE-165  WALEED AKRAM
# 
# 
# #2.6: GET METHOD
class Node:
    def __init__(self,p,i,n):
        self.prev = p
        self.item = i
        self.next = n


class DLList:
    def __init__(self):
        self.sentinel = Node(None , 63 , None)  #sentinel has address of Node
        self.sentinel.prev = self.sentinel  #sentinel.prev has address of sentinel since it has Node address and we had to point out to it
        self.sentinel.next = self.sentinel

    def AddLast(self ,i):
        new_last = Node(None , i ,None)  #1
        old_last =  self.sentinel.prev   #1
        new_last.prev = old_last   #2
        old_last.next = new_last    #3
        new_last.next = self.sentinel  #4 
        self.sentinel.prev = new_last  #5

    def AddFirst(self,i):
        new_first = Node(None ,i ,None)  
        old_first = self.sentinel.next
        new_first.prev = self.sentinel
        self.sentinel.next = new_first
        new_first.next = old_first
        old_first.prev = new_first

    def ToList(self):
        list = []
        current_node = self.sentinel.next
        while (current_node != self.sentinel):
            list.append(current_node.item)
            current_node = current_node.next
        return list

    def get(self ,i ): #here i is index ;not item
        if i<0:
            return None
        
        current_node = self.sentinel.next
        count = 0

        while(current_node != self.sentinel):
            if count == i:  #if we reach the desired index
                return current_node.item
            
            current_node = current_node.next
            count += 1

        return None


L = DLList()
L.AddLast(5)
L.AddLast(9)
L.AddLast(10)

L.AddFirst(3)

print(L.ToList())

assert(L.ToList() == [3,5,9,10])

print(L.get(1)) #index 1 has 5

#call test_get() method to verify if it works

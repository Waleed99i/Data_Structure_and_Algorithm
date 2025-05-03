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
        #definitions
        new_last = Node(None , i ,None)  #1
        old_last =  self.sentinel.prev   #1
        #new_last connections
        new_last.prev = old_last   #2
        #old_last becomes 2nd last
        old_last.next = new_last    #3
        new_last.next = self.sentinel  #4 
        #sentinel's previous points to new_last
        self.sentinel.prev = new_last  #5

    def AddFirst(self,i):
        new_first = Node(None ,i ,None)  
        old_first = self.sentinel.next
        #new_first connections
        new_first.prev = self.sentinel
        new_first.next = old_first
        #old_first becomes second
        old_first.prev = new_first
        #sentinel points to the new first
        self.sentinel.next = new_first

    def ToList(self):
        list = []
        current_node = self.sentinel.next
        while (current_node != self.sentinel):
            list.append(current_node.item)
            current_node = current_node.next
        return list

    def get(self ,i ): #here i is index ;not item hence its zero indexed ffr
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

    def RemoveLast(self):
        #def
        old_last = self.sentinel.prev
        new_last = old_last.prev
        #connections
        new_last.next = self.sentinel
        self.sentinel.prev = new_last

    def RemoveFirst(self):
        #def
        old_first = self.sentinel.next
        new_first = old_first.next
        #connections
        self.sentinel.next = new_first
        new_first.prev = self.sentinel
    
    def is_empty(self):
        if self.sentinel.next==self.sentinel:
            return True
        return False
    
    def size(self):
        current=self.sentinel.next
        count=0
        if current!=self.sentinel:
            count+=1
            current=current.next
        return count


L = DLList()
L.AddLast(5)
L.AddLast(9)
L.AddLast(10)

L.AddFirst(3)

#                             TEST
print("Before RemoveLast:", L.ToList())  

L.RemoveLast()
print("After RemoveLastt:", L.ToList())

L.RemoveFirst()
print("After RemoveFirst:", L.ToList())  

L.RemoveFirst()
print("After another RemoveFirst:", L.ToList())
L.RemoveFirst()
L.RemoveLast()
print(L.ToList())
L.AddFirst(3)
L.AddFirst(4)
L.AddFirst(5)
L.AddLast(6)
L.AddLast(7)
L.AddLast(8)
print(L.ToList())


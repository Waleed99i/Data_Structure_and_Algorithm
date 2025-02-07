#LAB 1
#2023-EE-165
#waleed akram

class Node:
    def __init__(self,i,n=None):
        self.item=i
        self.next=n
            
        
        
class SLList:
    def __init__(self):
        self.sentinal=Node(63)
        
        
L=SLList()

#%%

# Add_First
class Node:
    def __init__(self,i,n=None):
        self.item=i
        self.next=n
            
        
        
class SLList:
    def __init__(self):
        self.sentinal=Node(63)
        
    def AddFirst(self,i):
        self.New_Node=Node(i)
        self.New_Node.next=self.sentinal.next
        self.sentinal.next=self.New_Node
        
L=SLList()     
L.AddFirst(5)

#%%

#Add_Last
class Node:
    def __init__(self,i,n=None):
        self.item=i
        self.next=n
          
class SLList:
    def __init__(self):
        self.sentinal=Node(63)
        
    def AddFirst(self,i):
        self.New_Node=Node(i)
        self.New_Node.next=self.sentinal.next
        self.sentinal.next=self.New_Node
        
    def AddLast(self,i):
        p=self.sentinal
        while(p.next != None):
            p=p.next
        p.next=Node(i)
        
L=SLList()     
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)

#%%
#GET_First 
class Node:
    def __init__(self,i,n=None):
        self.item=i
        self.next=n
          
class SLList:
    def __init__(self):
        self.sentinal=Node(63)
        
    def AddFirst(self,i):
        self.New_Node=Node(i)
        self.New_Node.next=self.sentinal.next
        self.sentinal.next=self.New_Node
        
    def AddLast(self,i):
        p=self.sentinal
        while(p.next != None):
            p=p.next
        p.next=Node(i)
        
    def GetFirst(self):
        return self.sentinal.next.item
        
L=SLList()     
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)
A=L.GetFirst()

#%%
#Size
class Node:
    def __init__(self,i,n=None):
        self.item=i
        self.next=n
          
class SLList:
    def __init__(self):
        self.sentinal=Node(63)
        
    def AddFirst(self,i):
        self.New_Node=Node(i)
        self.New_Node.next=self.sentinal.next
        self.sentinal.next=self.New_Node
        
    def AddLast(self,i):
        p=self.sentinal
        while(p.next != None):
            p=p.next
        p.next=Node(i)
        
    def GetFirst(self):
        return self.sentinal.next.item
        
    def Size(self):
        x=0
        p=self.sentinal.next
        while(p != None):
            x+=1
            p=p.next
        return x
        
L=SLList()     
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)     
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)     
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)
L.AddFirst(50)
A=L.GetFirst()
B=L.Size()
print(A)
print(B)






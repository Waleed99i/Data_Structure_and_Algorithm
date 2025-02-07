#LAB2
#2023-EE-165  WALEED AKRAM

#2.1: THE CONSTRUCTOR
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

L = DLList()


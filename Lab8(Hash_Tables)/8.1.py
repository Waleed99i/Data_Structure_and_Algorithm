#2023-EE-165
#WALEED AKRAM
#LAB 8

#8.1
#vertex used in garphs mostly while node in general and in linked list thats why im using node instead of vertex
 
class Node:
    def __init__(self,x ,n):
        self.item = x
        self.next = n  # Pointer to the next vertex in the linked list


class HashT:
    def __init__(self): 
        self.M = 4 #M is the num of bins 
        self.n = 0 # n represents number of inserted items
        self.L = [() for x in range(self.M)] #python built in list 
   



H = HashT()


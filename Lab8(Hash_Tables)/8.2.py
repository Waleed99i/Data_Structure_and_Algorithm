#2023-EE-165
#WALEED AKRAM
#LAB 8

#8.2
class Node:
    def __init__(self,x ,n):
        self.item = x
        self.next = n  # Pointer to the next vertex in the linked list


class HashT:
    def __init__(self): 
        self.M = 4 #M is the num of bins 
        self.n = 0 # n represents number of inserted items
        self.L = [() for x in range(self.M)] #python built in list 
   
    def HashFunc(self ,x):
        '''
        as my instructor said that we can take any base for hash code
        i am taking 128 bcz it is preffered to take b >= 100
        also in python we can get ASCII by ord()
        '''
        if type(x) == int:
            return x
        
        elif type(x) == str:
            power = len(x) - 1
            y = 0
            for i in x:
                b = 128
                y += (ord(i)) * (b**power)
                power -= 1
            return y  #y is hash code
        else:
            raise TypeError("Key must be an integer or a string")


H = HashT()

#single line Test 
print(f"Hashcode for cat is: {H.HashFunc('cat')}" )

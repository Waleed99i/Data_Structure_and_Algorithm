#2023-EE-165
#WALEED AKRAM
#LAB 8


#8.4

def printHash(H):
    
    i = 0
    for item in H.L:
        
        if isinstance(item, Node):
            print(f'{i} -> ', end='')
            while (item.next != ()):
                print(item.item, '-' , end=' ')
                item = item.next
            print(f'{item.item}')
        else:
            print(f'{i} -> ')
        i += 1


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


    def insert(self, x):
        h = HashT.HashFunc(self, x)
        bin_num = h%self.M
        self.L[bin_num] = Node(x , self.L[bin_num])
        
        self.n += 1  #recall: n is number of inserted items in the hash table

        if self.n/self.M > 0.75:
            HashT.resize(self)

    def resize(self):
        new_M = 2 * self.M
        new_table = [() for x in range(new_M)]  # Initialize new table with empty tuples

        for i in self.L:  # Traverse each bucket in the old table(L)
            current = i
            while current != ():  # Traverse the linked list in the bucket
                '''HASH CODE '''
                h = HashT.HashFunc(self, current.item)  #.item bcz u know vertex/node is a key value pair , from current(=i of self.L) we'll get key but we want its value which is item extracted by .item
                ''' BIN NUMBER(bin_index)'''
                bin_index = h % new_M
                # Insert at the head of the new bucket (matches insert() logic)
                new_table[bin_index] = Node(current.item, new_table[bin_index])
                current = current.next

        self.L = new_table  # Update the table
        self.M = new_M      # Update the size/bin number
        
    def contains(self, x):
        h = HashT.HashFunc(self, x)
        bin_num = h % self.M
        n = self.L[bin_num]
        while n!= ():
            if n.item == x:
                return True
            n = n.next
        return False


H = HashT()

#single line Test 
#print(f"Hashcode for cat is: {H.HashFunc('cat')}" )
#L = [2, 3, 4, 'cat', 'dog', 'zebra']
#for x in L:
#    H.insert(x)
#printHash(H)

L = [7,16,3,11,20,13]
for x in L:
    H.insert(x)
printHash(H)

print(H.contains(3))
print(H.contains(8))

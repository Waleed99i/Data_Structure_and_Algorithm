#2023-EE-165
#WALEED AKRAM
#LAB 8


#8.5

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
   
    def HashFunc(self, x):
        '''
        Modified hash function to handle user-defined objects
        '''
        if isinstance(x, int):
            return x
        elif isinstance(x, str):
            power = len(x) - 1
            y = 0
            for i in x:
                b = 128
                y += (ord(i)) * (b**power)
                power -= 1
            return y
        elif hasattr(x, '__hash__'):  # For user-defined objects
            # Create a tuple of the object's attributes for hashing
            if hasattr(x, 'num') and hasattr(x, 'color'):  # Specific to baz class
                return hash((x.num, x.color))
            return hash(tuple(sorted(x.__dict__.items())))
        else:
            raise TypeError("Key must be an integer, string, or hashable object")

    def insert(self, x):
        h = self.HashFunc(x)  # Note: removed HashT. prefix since we're calling instance method
        bin_num = h % self.M
        # Check if item already exists before inserting
        if not self.contains(x):
            self.L[bin_num] = Node(x, self.L[bin_num])
            self.n += 1
            if self.n/self.M > 0.75:
                self.resize()

    def resize(self):
        a = [() for x in range(2*self.M)]
        index = 0
        x = 0
        while index < self.M:
            x = self.L[index]
            if self.L[index] == ():
                index += 1
            else:
                while x != ():
                    h = self.HashFunc(x.item)
                    bin_num = h % (2*self.M)
                    a[bin_num] = Node(x.item, a[bin_num])
                    x = x.next
                index += 1
                x = 0
        self.L = a
        self.M = 2*self.M

    def contains(self, x):
        h = self.HashFunc(x)
        bin_num = h % self.M
        n = self.L[bin_num]
        while n != ():
            if self._items_equal(n.item, x):
                return True
            n = n.next
        return False

    def _items_equal(self, item1, item2):
        '''
        Helper method to compare items properly, including user-defined objects
        '''
        if type(item1) != type(item2):
            return False
        if isinstance(item1, (int, str)):
            return item1 == item2
        # For user-defined objects
        if hasattr(item1, 'num') and hasattr(item1, 'color'):  # Specific to baz class
            return item1.num == item2.num and item1.color == item2.color
        # General case for other objects
        return vars(item1) == vars(item2)
    
    

#TESTING
class baz:
    def __init__(self, n, c):
        self.num = n
        self.color = c

# Test cases
H = HashT()
a = baz(2, 'red')
b = baz(2, 'blue')
c = baz(2, 'red')

H.insert(a)
H.insert(b)
H.insert(c)  # Should not insert duplicate of 'a'

print(H.contains(a))  # True
print(H.contains(b))  # True
print(H.contains(c))  # True (same as 'a')
printHash(H)  # Should show only two objects inserted (a and b, since c is duplicate of a)
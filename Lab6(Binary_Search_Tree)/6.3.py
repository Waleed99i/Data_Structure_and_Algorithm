#LAB 03
# 2023-EE-165
# WALEED AKRAM

#6.3 insert
class BSTMap:
    def __init__(self):
        self.root = None

    def i(r , k,v):
        #by recursion
        if (r == None): #smallest_problem
            return Vertex(k , v)
        else:
            if (k < r.key):
                sp1 = r.left
                sr1 = BSTMap.i(sp)
            
                r.left = sr1
            if(k > r.key):
                sp2 = r.right
                sr2 = BSTMap.i(sp2)

                r.right = sr2

class Vertex:
    def __init__(self , k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

    def insert(self,k,v):
        self.root = BSTMap.i(   ,k,v)

t = BSTMap()
Vertex(1 , 'uet')

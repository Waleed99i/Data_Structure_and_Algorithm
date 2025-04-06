# LAB -07
# 2023-EE-165
# WALEED AKRAM


# 7.6 The Insert Method
class Vertex:
    def __init__(self, k, v, color='b'):  # Default color is black 'b'
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.color = color  # New attribute for color representation


class RBTree:  #I used RBTMap instead of BSTMap for differentiation
    def __init__(self):
        self.root = None

    def rotate_left(self , root):
        if root.right is not None:
            # Step 1: Store the right child
            child = root.right  
            
            # Step 2: Move the left child of the right node to be the right child of the current root
            root.right = child.left  
            
            # Step 3: Make the current root the left child of the right child
            child.left = root  
        
            root = child  
        else:
            raise ValueError("Node cannot be rotated left; no right child available.")

    
    def rotate_right(self , root):
        if root.left is not None:
            # Step 1: Store the left child
            child = root.left  
            
            # Step 2: Move the right child of the left node to be the left child of the current root
            root.left = child.right  

            # Step 3: Make the current root the right child of the left child
            child.right = root  
      
            root = child  
        else:
            raise ValueError("Node cannot be rotated right; no left child available.")



    def color_flip(self, node):
        """
        Flips the color of the given node and its children.
        
        Assumes:
        - The node is black and its children are red.
        """
        if node is not None:
            # Flip color of the parent node
            node.color = 'r' if node.color == 'b' else 'b'
            '''
            it equals
            if node.color == 'b':
                node.color = 'r'
            else:
                node.color = 'b'
            '''
            # Flip color of the left child if it exists
            if node.left is not None:
                node.left.color = 'b' if node.left.color == 'r' else 'r'
            
            # Flip color of the right child if it exists
            if node.right is not None:
                node.right.color = 'b' if node.right.color == 'r' else 'r'


    def insert(self, key, value):
        # Step 1: Insert using BST-like behavior and then set the color of the new node to red
        self.root = self._insert(self.root, key, value)
        self.root.color = 'b'  # Ensure the root is always black after insertion

    def _insert(self, node, key, value):
        #    ---- STEP 1:using old BST (from lab 6) ----
        # Perform BST insertion(just instead of r,k,v ; I am using node,key,value for better understanding)
        #RECURSION
        # Base case: if the current node is None, create a new Vertex
        if node is None:
            return Vertex(key, value, color='r')  # New vertex is red(RULE 1)
       
        else:
            # If the (incoming) key is less than the current node's/root's key, go left
            if key < node.key:
                smaller_problem1 = node.left
                smaller_result1 = self._insert(smaller_problem1,key,value) # Call function and give smaller_problem1 as argument
                #now to connect
                node.left = smaller_result1
            
            # If the (incoming) key is greater than the current node's/root's key, go right
            elif key > node.key:
                smaller_problem2 = node.right
                smaller_result2 = self._insert(smaller_problem2,key,value) # Call function and give smaller_problem2 as argument
                #now to connect
                node.right = smaller_result2

            else:
                # If the key already exists, update its value
                node.value = value


        #   ---- STEP 2: implementing 4 rules for LLRBTree insertion ----
        # RULE 1 ALREADY IMPLEMENTED ABOVE

        # Rule 2: A Right Red Vertex ---> rotate_left
        if node.right is not None and node.right.color == 'r' and (node.left is None or node.left.color == 'b'):
            node = self.rotate_left(node)

        # Rule 3: Two Left Red Vertices ---> rotate_right
        if node.left is not None and node.left.color == 'r' and node.left.left is not None and node.left.left.color == 'r':
            node = self.rotate_right(node)

        # Rule 4: Color Flip
        if node.left is not None and node.left.color == 'r' and node.right is not None and node.right.color == 'r':
            self.color_flip(node)

        return node
    


# function calling has left , will do it afterwards 


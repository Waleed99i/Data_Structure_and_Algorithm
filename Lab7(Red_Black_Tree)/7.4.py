# LAB -07
# 2023-EE-165
# WALEED AKRAM


# 7.4  The RotateLeft Method
class Vertex:
    def __init__(self, k, v, color='b'):  # Default color is black 'b'
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.color = color  # New attribute for color representation


class RBTree:  #i used RBTMap instead of BSTMap for differentiation
    def __init__(self):
        self.root = None

    def rotate_left(self, root):
        if root.right is not None:
            # Step 1: Store the right child
            child = root.right  
            
            # Step 2: Move the left child of the right node to be the right child of the current root
            root.right = child.left  
            
            # Step 3: Make the current root the left child of the right child
            child.left = root  
        
            return child  # Return the new root after rotation
        else:
            raise ValueError("Node cannot be rotated left; no right child available.")

    
    def rotate_right(self, root):
        if root.left is not None:
            # Step 1: Store the left child
            child = root.left  
            
            # Step 2: Move the right child of the left node to be the left child of the current root
            root.left = child.right  

            # Step 3: Make the current root the right child of the left child
            child.right = root  
      
            return child  # Return the new root after rotation
        else:
            raise ValueError("Node cannot be rotated right; no left child available.")




"""
#     ----------before i used self. with node-----------

    def rotate_left(self , node):
       if self.node.right is not None:
           # Step 1: Store the right child
           child = self.node.right  
           
           # Step 2: Move the left child of the right node to be the right child of the current root
           self.node.right = child.left  
           
           # Step 3: Make the current root the left child of the right child
           child.left = self.node  
           
           # Step 4: Update the root to the new child
           self.node = child  
       else:
           raise ValueError("Node cannot be rotated left; no right child available.")

"""


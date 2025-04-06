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
    
    def rotate_right(self , node):
        if node.left is not None:
            # Step 1: Store the left child
            child = node.left  
            
            # Step 2: Move the right child of the left node to be the left child of the current root
            node.left = child.right  

            # Step 3: Make the current root the right child of the left child
            child.right = node  
            
            # Step 4: Update the root to the new child
            node = child  
        else:
            raise ValueError("Node cannot be rotated right; no left child available.")




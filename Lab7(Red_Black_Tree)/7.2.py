# LAB -07
# 2023-EE-165
# WALEED AKRAM


 # 7.2 The Constructor of BSTMap Class
class Vertex:
    def __init__(self, k, v, color='b'):  # Default color is black 'b'
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.color = color  # New attribute for color representation


class RBTree:  #i used RBTree instead of BSTMap for differentiation
    def __init__(self):
        self.root = None



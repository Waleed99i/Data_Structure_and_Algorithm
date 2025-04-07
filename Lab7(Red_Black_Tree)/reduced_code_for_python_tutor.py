# LAB -07
# 2023-EE-165
# WALEED AKRAM

class Vertex:
    def __init__(self, k, v, color='b'):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.color = color

class RBTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, root):
        child = root.right
        root.right = child.left
        child.left = root
        return child

    def rotate_right(self, root):
        child = root.left
        root.left = child.right
        child.right = root
        return child

    def color_flip(self, node):
        node.color = 'r' if node.color == 'b' else 'b'
        if node.left: node.left.color = 'b' if node.left.color == 'r' else 'r'
        if node.right: node.right.color = 'b' if node.right.color == 'r' else 'r'

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = 'b'

    def _insert(self, node, key, value):
        if node is None:
            return Vertex(key, value, color='r')
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value

        if node.right and node.right.color == 'r' and (not node.left or node.left.color == 'b'):
            node = self.rotate_left(node)
        if node.left and node.left.color == 'r' and node.left.left and node.left.left.color == 'r':
            node = self.rotate_right(node)
        if node.left and node.left.color == 'r' and node.right and node.right.color == 'r':
            self.color_flip(node)

        return node

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

# Function calls to test the insertion and find methods
if __name__ == "__main__":
    T = RBTree()
    T.insert(10, "Value 10")
    T.insert(20, "Value 20")
    T.insert(30, "Value 30")
    T.insert(15, "Value 15")
    T.insert(25, "Value 25")

    # Test the find method
    print(T.find(10))  # Should return True
    print(T.find(15))  # Should return True
    print(T.find(100)) # Should return False
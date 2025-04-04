#LAB 06
# 2023-EE-165
# WALEED AKRAM

class Vertex:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None

    # Insert method
    def insert(self, k, v):
        self.root = self._insert(self.root, k, v)

    def _insert(self, r, k, v):
        # Using RECURSION
        # Base case: if the current node is None, create a new Vertex
        if r is None:
            return Vertex(k, v)
        else:
            # If the (incoming) key is less than the current node's/root's key, go left
            if k < r.key:
                smaller_problem1 = r.left
                smaller_result1 = self._insert(smaller_problem1, k, v)  # Call function and give smaller_problem1 as argument
                # Now to connect
                r.left = smaller_result1

            # If the key is greater than the current node's key, go right
            elif k > r.key:
                smaller_problem2 = r.right
                smaller_result2 = self._insert(smaller_problem2, k, v)  # Call function and give smaller_problem2 as argument
                # Now to connect
                r.right = smaller_result2

            # If the key already exists, you can choose to update the value
            else:
                r.value = v  # Update the value if the key already exists
        return r



# Example usage
t = BSTMap()
t.insert(4, 'uet')
t.insert(2, 'uet')
t.insert(7, 'uet')
t.insert(1, 'uet')
t.insert(3, 'uet')
t.insert(5, 'uet')
t.insert(8, 'uet')


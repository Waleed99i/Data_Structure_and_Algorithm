class swap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap(self):
        self.a, self.b = self.b, self.a
        return self.a, self.b
    
    def __str__(self):
        return f"swap({self.a}, {self.b})"
    


s = swap(1, 2)
print(s.swap())


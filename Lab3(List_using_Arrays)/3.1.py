#LAB 3
#2023-EE-165
#WALEED AKRAM

#3.1 CONSTRUCTOR
import array as arr

class AList:
    def __init__(self):
        self.capacity = 10  # Start with a smaller initial capacity for testing
        self.item = arr.array('i', [0 for x in range(self.capacity)])
        self.current_size = 0

a = AList()

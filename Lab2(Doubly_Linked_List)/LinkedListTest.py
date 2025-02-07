#2.3:Testing

from LinkedListDeque import *

L = DLList()
L.AddLast(5)
L.AddLast(9)
L.AddLast(10)

L.AddFirst(3)
assert(L.ToList() == [3,5,9,10])





 
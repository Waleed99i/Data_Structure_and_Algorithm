#2023-EE-165
# waleed akram


class Graph:
    def __init__(self, V):
        self.v = V
        self.e = 0
        self.L = [[] for x in range(self.v)]

    def AddEdge(self, v, w):
        self.L[v].append(w)  # Only add edge from v to w for directed graph
        self.e += 1


    def edges(self):
        """Returns the number of edges in the graph."""
        return self.e

#                                   TEST CASES
g = Graph(5)
g.AddEdge(2, 3)
g.AddEdge(2, 1)
g.AddEdge(1, 0)
g.AddEdge(1, 4)
print(g.L)

print("Number of edges:", g.edges())  # 4


# not in manual , just writing for my practice

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

    def vertices(self):
        """Returns the number of vertices in the graph."""
        return self.v

    def degree(self, v):
        """Returns the degree of vertex v in the graph."""
        if v < 0 or v >= self.v: #seldf.v is the number of vertices(instnace variable of class Graph)
            raise ValueError("Vertex out of bounds")
        return len(self.L[v])

    def connected(self, s, t):
        L = []
        L.append(s)
        if s == t:
            return True
        v = L[0]
        i = 0
        while len(L) != self.v:
            for x in self.L[v]:
                if x not in L:
                    L.append(x)
                    if x == t:
                        return True
            i += 1
            if i >= len(L):  # Prevent index out of range error
                break
            v = L[i]
        return False

#                                   TEST CASES
g = Graph(5)
g.AddEdge(2, 3)
g.AddEdge(2, 1)
g.AddEdge(1, 0)
g.AddEdge(1, 4)
print(g.L)
print(g.connected(3, 0))  # False, as the graph is directed
print(g.connected(2, 0))  # True
print(g.connected(3, 1))  # False
print("Number of edges:", g.edges())  # 4
print("Number of vertices:", g.vertices())  # 5
print("Degree of vertex 1:", g.degree(1))  # 2


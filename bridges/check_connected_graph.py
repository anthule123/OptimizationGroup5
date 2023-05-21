class CheckConnectedGraph:
    def __init__(self, edges_set, nvertex):
        self.edges_set = edges_set
        self.nvertex = nvertex
        self.parent = [i for i in range(nvertex)]
        self.rank = [0 for i in range(nvertex)]
        self.count = nvertex
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u!=v:
            if self.rank[u] < self.rank[v]:
                u, v = v, u
            self.parent[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1
            self.count -= 1
    def check_connected_graph(self):
        for u, v in self.edges_set:
            self.union(u, v)
        return self.count == 1
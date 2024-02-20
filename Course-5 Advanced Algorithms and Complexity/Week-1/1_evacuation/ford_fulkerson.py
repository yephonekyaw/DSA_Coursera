# with depth-first-search
# vertices are alphabets

class Edge(object):
    def __init__(self, u, v, capacity):
        self.source = u
        self.sink = v
        self.capacity = capacity
    
    def __repr__(self):
        return "%s-->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
    
    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]
    
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path, path_set):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            # print(edge)
            residual = edge.capacity - self.flow[edge]
            # print(residual)
            if residual > 0 and not (edge, residual) in path_set:
                path_set.add((edge, residual))
                result = self.find_path(edge.sink, sink, path + [(edge, residual)], path_set)
                
                if result != None:
                    return result
        
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [], set())
        while path != None:
            # print(path)
            flow = min(res for edge,res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [], set())
        return sum(self.flow[edge] for edge in self.get_edges(source))

g = FlowNetwork()
for char in "sopqrt":
    g.add_vertex(char)

g.add_edge('s', 'o', 3)
g.add_edge('s', 'p', 3)
g.add_edge('o', 'p', 2)
g.add_edge('o', 'q', 3)
g.add_edge('p', 'r', 2)
g.add_edge('r', 't', 3)
g.add_edge('q', 'r', 4)
g.add_edge('q', 't', 2)

print(g.adj)
print(g.max_flow('s', 't'))
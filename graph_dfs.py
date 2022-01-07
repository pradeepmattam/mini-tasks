from collections import defaultdict

class Graph:

    def __init__(self):
        self.dict = defaultdict(list)

    def add_edge(self, v, e):
        self.dict[v].append(e)

    def depth_first_traversal(self, vertex, visited):
        if vertex in visited:
            return
        visited.append(vertex)
        for new_vertex in self.dict[vertex]:
            if new_vertex not in visited:
                self.depth_first_traversal(new_vertex, visited)

g = Graph()

g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('1', '2')
g.add_edge('2', '0')
g.add_edge('2', '3')
g.add_edge('3', '3')

visited = list()

g.depth_first_traversal('2', visited)

print("depth first: ", end=" ")
print(visited)



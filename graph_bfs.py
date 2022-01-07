from collections import defaultdict

class Graph:

    def __init__(self):
        self.dict = defaultdict(list)

    def add_edge(self, v, e):
        self.dict[v].append(e)

    def breadth_first_traversal(self, vertex, visited, stack):
        if vertex in visited:
            return
        visited.append(vertex)
        stack.append(vertex)
        while len(stack) !=0:
            adj_vertex = stack.pop()
            for neighbor in self.dict[adj_vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)




g = Graph()

g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('1', '2')
g.add_edge('2', '0')
g.add_edge('2', '3')
g.add_edge('3', '3')

visited = list()
stack = list()
g.breadth_first_traversal('2', visited, stack)

print("breadth first: ", end=" ")
print(visited)



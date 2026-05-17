from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def insert_edge(self, x, y, weight=0):
        self.graph[x].append((y, weight))

        if not self.directed:
            self.graph[y].append((x, weight))

    def insert_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []


    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []

        for u in self.graph:
            for v, w in self.graph[u]:
                edges.append((u, v, w))

        return edges

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)

            for neighbor, _ in self.graph[u]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


    def dfs(self, start):
        visited = set()
        order = []

        def dfs_helper(u):
            visited.add(u)
            order.append(u)

            for neighbor, _ in self.graph[u]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)

        return order





if __name__ == "__main__":
    g = Graph()
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 3)
    g.insert_edge(2, 4)

    print(g.get_vertices())

    print(g.get_edges())

    print(g.bfs(0))

    print(g.dfs(0))


from collections import deque


def topological_sort_dfs(graph):
    visited = set()
    rec_stack = []
    order_stack = []

    def dfs(node):
        visited.add(node)
        rec_stack.append(node)

        for neighbor, _ in graph.graph[node]:
            if neighbor in rec_stack:
                raise ValueError("Cycle Detected: Not a DAG")

            if neighbor not in visited:
                dfs(neighbor)

        rec_stack.remove(node)
        order_stack.append(node)

    for vertex in graph.get_vertices():
        if vertex not in visited:
            dfs(vertex)

    return order_stack[::-1]


def topological_sort_kahn(graph, vertices):

    in_degree = {vertex: 0 for vertex in vertices}

    for u in graph:
        for v, _ in graph[u]:  # (v, w) -> vertices, weight
            in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour, _ in graph[node]:
            in_degree[neighbour] -= 1

            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(result) != len(vertices):
        raise ValueError("Cycle Detected: Not a DAG")

    return result

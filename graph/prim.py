import heapq

from graph import Graph


def prim(graph, start):
    mst = []
    visited = {start}
    edges = []

    for neighbour, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbour))

    while len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)

        if v in visited:
            continue

        mst.append((u, v, weight))
        visited.add(v)

        for neighbour, weight in graph[v]:
            if neighbour not in visited:
                heapq.heappush(edges, (weight, v, neighbour))

    return mst


if __name__ == "__main__":
    g = Graph()
    g.insert_edge("A", "B", 2)
    g.insert_edge("A", "C", 3)
    g.insert_edge("C", "D", 5)
    g.insert_edge("B", "D", 4)

    print(prim(g.graph, "B"))

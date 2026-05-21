from graph import Graph


def floyd_warshall(graph):
    V = len(graph)

    dist = [[float("inf")] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # for i in range(V):
    #     for j in range(V):
    #         for k in range(V):
    #             if dist[j][k] > dist[j][i] + dist[i][k]:
    #                 dist[j][k] = dist[j][i] + dist[i][k]

    print(dist)


if __name__ == "__main__":
    g = Graph()
    g.insert_edge(0, 1, 3)
    g.insert_edge(0, 2, 2)
    g.insert_edge(1, 2, 4)
    g.insert_edge(0, 1, 3)
    g.insert_edge(2, 2, 1)

    floyd_warshall(g.graph)

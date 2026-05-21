"""
Dijkstra's Algorithm (Shortest Path)

Time Complexity	    Space	Use Case	                            Key Insight
DO((V+E) log V)	    O(V)	Single-source, non-negative weights	    Greedy with priority queue


"""

import heapq

from graph import Graph


def dijkstra(graph, start):

    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]  # (distance, vertex)
    prev = {vertex: None for vertex in graph}

    while pq:
        curr_distance, node = heapq.heappop(pq)

        if curr_distance > distances[node]:
            continue

        for neighbour, weight in graph[node]:
            distance = curr_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                prev[neighbour] = node
                heapq.heappush(pq, (distance, neighbour))

    return distances, prev


if __name__ == "__main__":
    print("Dijkstra \n")
    g2 = Graph()
    g2.insert_edge("A", "B", 4)
    g2.insert_edge("A", "D", 2)
    g2.insert_edge("B", "C", 1)
    g2.insert_edge("B", "E", 3)
    g2.insert_edge("D", "E", 5)

    print(dijkstra(g2.graph, "A"))

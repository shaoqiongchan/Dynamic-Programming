import heapq

graph_dict = {'A': {'B': 5, 'C': 1},
              'B': {'A': 5, 'C': 2, 'D': 1},
              'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
              'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
              'E': {'C': 8, 'D': 3},
              'F': {'D': 3},
              }


def dijkstra(graph, s):
    p_queue = [(0, s)]
    visited = {s}
    parent = {s: None}
    distance = {s: 0}
    while len(p_queue) > 0:
        (dis, vertex) = heapq.heappop(p_queue)
        visited.add(vertex)
        print(vertex)
        nodes = graph[vertex].keys()
        for n in nodes:
            if n not in visited:
                if dis + graph[vertex][n] < distance.get(n, 100000):
                    heapq.heappush(p_queue, (dis + graph[vertex][n], n))
                    distance[n] = dis + graph[vertex][n]
                    parent[n] = vertex
    return parent, distance


parent_dict, distance_dict = dijkstra(graph_dict, 'A')
print(parent_dict, distance_dict)

v = 'B'
while v is not None:
    print(v)
    v = parent_dict[v]

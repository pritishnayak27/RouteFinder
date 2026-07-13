import heapq

def dijkstra(graph, start, end):

    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    previous = {}

    while queue:

        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):

            edge = graph[current_node][neighbor]
            weight = edge["travel_time"]

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(
                    queue,
                    (distance, neighbor)
                )

    path = []

    node = end

    while node != start:

        path.append(node)
        node = previous[node]

    path.append(start)

    path.reverse()

    return path, distances[end]
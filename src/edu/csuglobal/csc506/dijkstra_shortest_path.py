import heapq

# Predefined graph structure
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 1, 'E': 7},
    'D': {'B': 4, 'C': 1, 'E': 3},
    'E': {'C': 7, 'D': 3}
}

def print_graph_ascii(graph):
    print("Graph structure (ASCII view):\n")
    for node in graph:
        edges = ", ".join([f"{neighbor}({weight})" for neighbor, weight in graph[node].items()])
        print(f"{node} --> {edges}")
    print("\n")

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, end):
    path = []
    while end:
        path.insert(0, end)
        end = previous_nodes[end]
    return path

def main():
    print_graph_ascii(graph)

    print("Available nodes:", ", ".join(graph.keys()))
    start = input("Enter the start node: ").strip().upper()
    end = input("Enter the end node: ").strip().upper()

    if start not in graph or end not in graph:
        print("Invalid start or end node.")
        return

    distances, previous_nodes = dijkstra(graph, start)
    path = reconstruct_path(previous_nodes, end)

    print(f"\nShortest path from {start} to {end}: {' → '.join(path)}")
    print(f"Total distance: {distances[end]}")

if __name__ == "__main__":
    main()

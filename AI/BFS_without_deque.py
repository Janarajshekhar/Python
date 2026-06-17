graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
queue = []              # Queue using list
visited = set()         # Store visited nodes
traversal_order = []    # Store BFS order
start_node = 'A'
queue.append(start_node)
visited.add(start_node)
while queue:
    current = queue.pop(0)      # Remove first element
    traversal_order.append(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
print("\nFinal Traversal Order:")
print("  -->  ".join(traversal_order))
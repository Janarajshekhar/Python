from collections import deque
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : []
}
queue = deque()
visited = set()
traversal_order = []
start_node = 'A'
queue.append(start_node)
visited.add(start_node)
while queue : 
    current = queue.popleft()
    traversal_order.append(current)
    for neighbor in graph[current] :
        if neighbor not in visited :
            queue.append(neighbor)
            visited.add(neighbor)
print("\n Final traversal order : ")
print("  -->  ".join(traversal_order))
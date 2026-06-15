from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
queue = deque()         
visited = set()          
traversal_order = []
start_node = 'A'
queue.append(start_node)   # Enqueue node A
visited.add(start_node)    # Mark A as visited
while queue :
    current = queue.popleft()            
    traversal_order.append(current)      
    for neighbor in graph[current] :      
        if neighbor not in visited :
            queue.append(neighbor)       # Enqueue unvisited neighbor
            visited.add(neighbor)    
print("\n Final Traversal Order : ")
print("  -->  ".join(traversal_order))
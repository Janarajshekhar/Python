graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : ['H', 'I'],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : []
}

visited = set()
traversal_order = []
def dfs(node) :
    if node not in visited:
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)
dfs('A')
print("traversal order : ")
print("  -->  ".join(traversal_order))
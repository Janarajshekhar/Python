graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : ['I', 'J'],
    'F' : [],     
    'G' : ['K', 'L'],
    'H' : [],
    'I' : ['M', 'N'],
    'J' : [],
    'K' : ['O', 'P'],
    'L' : ['Q'],
    'M' : [],
    'N' : [],
    'O' : [],
    'P' : [],
    'Q' : []
}
visited = set()
traversal_order = []
def dfs(node):
    if node not in visited :
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node] :
            dfs(neighbor)
dfs('A')
print("\n Final traversal order : ")
print("  -->  ".join(traversal_order))
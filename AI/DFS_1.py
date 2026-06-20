# graph = {
#     'A' : ['B', 'C'],
#     'B' : ['D', 'E'],
#     'C' : ['F', 'G'],
#     'D' : [],
#     'E' : [],
#     'F' : [],     
#     'G' : []
# }
graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E', 'F'],
    'D' : [],
    'E' : [],
    'F' : [],     
    # 'G' : []
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
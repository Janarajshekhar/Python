# Complete AO* Algorithm in Python
graph = {
    'A': [(['B'], 1), (['C', 'D'], 2)],
    'B': [(['E'], 1), (['F'], 2)],
    'C': [(['G'], 2)],
    'D': [(['H'], 1)]
}
h = {'A': 10, 'B': 4, 'C': 6, 'D': 5, 'E': 0, 'F': 0, 'G': 0, 'H': 0
}
solved = {}
solution = {}
def ao_star(node):
    # Goal node
    if node not in graph:
        solved[node] = True
        return h[node]
    print("Expanding:", node)
    min_cost = float('inf')
    best_child = None
    # Check all possible AND/OR paths
    for children, cost in graph[node]:
        total_cost = cost
        for child in children:
            total_cost += h[child]
        if total_cost < min_cost:
            min_cost = total_cost
            best_child = children
    # Update heuristic value
    h[node] = min_cost
    # Store best solution
    solution[node] = best_child
    # Expand selected nodes
    all_solved = True
    for child in best_child:
        if child in graph:
            ao_star(child)
        if child not in solved:
            all_solved = False
    # Mark solved
    if all_solved:
        solved[node] = True
    return h[node]
def print_solution(node):
    print(node, end="")
    if node in solution:
        for child in solution[node]:
            print(" -> ", end="")
            print_solution(child)
# Start AO*
cost = ao_star('A')
print("\nOptimal Solution Path:")
print_solution('A')
print("\n\nMinimum Cost:", cost)
print("\nUpdated Heuristic Values:")
print(h)
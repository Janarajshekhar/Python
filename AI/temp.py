import heapq
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 3), ("E", 1)],
    "C": [("F", 5), ("E", 1)],
    "D": [],
    "E": [("G", 2)],
    "F": [("G", 1)],
    "G": []
}
heuristic = {
    "A": 7,
    "B": 6,
    "C": 2,
    "D": 1,
    "E": 0,
    "F": 1,
    "G": 0
}
start = 'A'
goal = 'E'
pq = [(heuristic[start], 0, start, [])]
while pq :
    f, g, node, path = heapq.heappop(pq)
    path = path + [node]
    if node == goal :
        print("path : ","  -->  ".join(path))
        print("cost : ", g)
        break
    for neighbor_node, cost in graph[node] :
        new_cost = g + cost
        f = new_cost + heuristic[neighbor_node]
        heapq.heappush(pq, (f, new_cost, neighbor_node, path))
import heapq
# graph = {
#     'S':[('A',1),('B',2)],
#     'A':[('X',4),('Y',7)],
#     'B':[('C',7),('D',1)],
#     'C':[('E',5)],
#     'D':[('E',12)],
#     'X':[('E',2)],
#     'Y':[('E',3)],
#     'E':[]
# }
# heuristic = {
#     'S':15,
#     'A':5,
#     'B':6,
#     'C':4,
#     'D':15,
#     'X':5,
#     'Y':8,
#     'E':0
# }
# start = 'S'
# goal = 'E'

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
start = "A"
goal = "E"
pq = [(heuristic[start], 0, start, [])]
while pq:
    f, g, node, path = heapq.heappop(pq)
    path = path + [node]
    if node == goal :
        print("Path:", " -> ".join(path))
        print("Cost:", g)
        break
    for current_node, cost in graph[node]:
        new_cost = g + cost
        f = new_cost + heuristic[current_node]
        heapq.heappush(pq, (f, new_cost, current_node, path))
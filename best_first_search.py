graph1 = {
    "A": {"B": 3, "C": 2, "D": 4, "E": 6},
    "B": {"F": 4, "G": 7},
    "C": {"H": 3, "I": 5},
    "D": {"J": 2, "K": 6},
    "E": {"L": 4, "M": 8},
    "F": {"N": 5},
    "G": {"O": 3},
    "H": {"P": 8},
    "I": {"P": 4},
    "J": {"Q": 6},
    "K": {"Q": 2},
    "L": {"R": 7},
    "M": {"R": 3},
    "N": {},
    "O": {},
    "P": {},
    "Q": {},
    "R": {}
}

heuristic1 = {
    "A": 14, "B": 12, "C": 10, "D": 8, "E": 7,
    "F": 11, "G": 8, "H": 9, "I": 6, "J": 7, "K": 4,
    "L": 5, "M": 2, "N": 9, "O": 5, "P": 4, "Q": 3,
    "R": 0
}

graph2 = {
    "S": {"A": 4, "B": 2},
    "A": {"C": 6, "D": 3},
    "B": {"E": 5, "F": 7},
    "C": {"G": 4},
    "D": {"G": 6, "H": 8},
    "E": {"H": 2},
    "F": {"H": 3},
    "G": {"Z": 5},
    "H": {"Z": 4},
    "Z": {}
}

heuristic2 = {
    "S": 12,
    "A": 10, "B": 8,
    "C": 6, "D": 7,
    "E": 5, "F": 9,
    "G": 4, "H": 3,
    "Z": 0
}

def greedy_best_first(start, goal):
    path = []
    currentNode = start
    currentNodeHeuristics = heuristic[start]
    path.append(currentNode)
    while currentNode != goal:
        nodeWithBestHeuristics = None
        for node in graph[currentNode].keys():
            if nodeWithBestHeuristics == None:
                nodeWithBestHeuristics = node
            elif heuristic[nodeWithBestHeuristics]> heuristic[node]:
                nodeWithBestHeuristics = node
        currentNode = nodeWithBestHeuristics
        path.append(currentNode)
    return path

def path_to_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost+=graph[path[i]][path[i+1]]
    return cost
graph = graph1
heuristic = heuristic1
path = greedy_best_first("A", "R")
print(f"Path : {path}")
print(f"Cost : {path_to_cost(path)}")
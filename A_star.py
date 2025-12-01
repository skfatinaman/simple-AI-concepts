import distanceGraph
import heapq

def aStartSearch(graph,heuristics, start, goal):
    minHeap = [(heuristics[start],0,start)]
    parent = {start : None}
    distance = {start : 0}
    while minHeap:
        goodness, cost, node = heapq.heappop(minHeap)
        if node == goal :
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, cost
        for neighbor, newCost in graph[node].items():
            totalCost = cost + newCost
            if neighbor not in distance.keys() or distance[neighbor] > totalCost:
                heapq.heappush(minHeap, (totalCost+heuristics[neighbor], totalCost, neighbor))
                parent[neighbor] = node
                distance[neighbor] = totalCost
    return None, None

graph = distanceGraph.graph
start = "A"
goal = "L"
heuristics = distanceGraph.heuristicsFunction(distanceGraph.coordinates, goal)

path, cost = aStartSearch(graph,heuristics, start, goal)
print(f"The path is : {path}")
print(f"The cost is : {cost}")
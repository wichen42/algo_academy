from collections import deque, defaultdict
# Write a function, shortest_path that takes in a list of edgges for an undirected graph and two nodes (node_A, node_B). 
# The function should return the length of the shortest path between A and B.
# Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A), 0])
    
    while queue:
        node, distance = queue.popleft()
        
        if node == node_B:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance+1))
    
    return -1
    
def build_graph(edges):
    graph = defaultdict(list)
from collections import defaultdict, deque
# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]

def shortestAlternatingPath(n, redEdges, blueEdges):
    red = defaultdict(list)
    blue = defaultdict(list)

    for src, dst in redEdges:
        red[src].append(dst)
    for src, dst in blueEdges:
        blue[src].append(dst)

    # initialize queue with starting node
    answer = [-1 for _ in range(n)]
    queue = deque([(0,0,None)]) # (node, length, prev_edge_color)
    visited = set([(0, None)]) # (node, prev_edge_color)

    while queue:
        # shift current node out from queue
        node, length, edgeColor = queue.popleft()

        # process node
        if answer[node] == -1:
            answer[node] = length
        # push all valid neighbors into queue
        if edgeColor != "RED": # not red b/c we start with None
            for neighbor in red[node]:
                if (neighbor, "RED") not in visited:
                    visited.add((neighbor, "RED"))
                    queue.append((neighbor, length+1, "RED"))
        if edgeColor != "BLUE":
            for neighbor in blue[node]:
                if (neighbor, "BLUE") not in visited:
                    visited.add((neighbor, "BLUE"))
                    queue.append((neighbor, length+1, "BLUE"))

        


    return answer
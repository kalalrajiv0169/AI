# Implement Depth-First Search (DFS) to traverse a graph.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    
    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            new_path = dfs(node, goal, path)
            if new_path:
                return new_path
                
    return None

# Find path from 'A' to 'F'
print("DFS path from 'A' to 'F':", dfs('A', 'F'))

"""
Breadth-First Search (BFS) Template

Use for shortest path, level-order traversal, graph exploration.
Time Complexity: O(V + E) for graphs, O(n) for trees
Space Complexity: O(w) where w = max width of tree/graph
"""

from collections import deque


# ============ TREE BFS ============

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    """
    Level-order (breadth-first) tree traversal.
    Returns list of lists, one list per level.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


# ============ GRAPH BFS ============

def graph_bfs(graph, start):
    """
    BFS on graph using adjacency list.
    graph: dict where graph[node] = [neighbors]
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# ============ SHORTEST PATH ============

def shortest_path_unweighted(graph, start, end):
    """
    Find shortest path in unweighted graph.
    Returns list of nodes forming shortest path.
    """
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []  # No path found


# ============ 2D GRID BFS ============

def shortest_path_grid(grid, start, end):
    """
    Shortest path in 2D grid (0 = obstacle, 1 = free).
    Returns distance or -1 if unreachable.
    """
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return -1
    
    visited = set([start])
    queue = deque([(start[0], start[1], 0)])  # row, col, distance
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 1 and (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1  # Unreachable


# ============ MULTI-SOURCE BFS ============

def multi_source_bfs(grid):
    """
    Find shortest distance from each cell to nearest source.
    Example: Rotten Oranges problem
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    
    # Start from all sources
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Source cell
                queue.append((r, c, 0))
                visited.add((r, c))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return queue  # Or process as needed


# ============ TOPOLOGICAL SORT (BFS - Kahn's Algorithm) ============

def topological_sort_bfs(n, edges):
    """
    Topological sort using Kahn's algorithm (BFS).
    edges: list of [from, to] pairs
    Returns topological order or empty if cycle exists.
    """
    # Build adjacency list and in-degree
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Queue contains nodes with no incoming edges
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    return result if len(result) == n else []


# Example problems:
# - Binary Tree Level Order Traversal
# - Number of Islands
# - Shortest Path in Grid
# - Rotting Oranges
# - Word Ladder
# - Course Schedule II (Topological Sort)

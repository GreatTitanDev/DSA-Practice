"""
Depth-First Search (DFS) Template

Use for tree/graph traversal, backtracking problems.
Time Complexity: O(V + E) for graphs, O(n) for trees
Space Complexity: O(h) recursion stack, where h = height
"""


# ============ TREE DFS ============

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """
    Inorder: Left -> Node -> Right
    For BST: gives sorted order
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result


def preorder_traversal(root):
    """
    Preorder: Node -> Left -> Right
    Often used for copying tree
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result


def postorder_traversal(root):
    """
    Postorder: Left -> Right -> Node
    Often used for deletion
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result


# ============ GRAPH DFS ============

def graph_dfs(graph, start):
    """
    DFS on graph using adjacency list.
    graph: dict where graph[node] = [neighbors]
    """
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start)
    return result


# ============ BACKTRACKING TEMPLATE ============

def backtrack(candidates, target, start=0, path=None, result=None):
    """
    General backtracking template.
    Example: Combination Sum, Permutations, N-Queens
    """
    if path is None:
        path = []
    if result is None:
        result = []
    
    # Base case: found solution
    if target == 0:
        result.append(path[:])
        return
    
    # Prune: impossible to reach target
    if target < 0:
        return
    
    # Try each candidate
    for i in range(start, len(candidates)):
        # Choose
        path.append(candidates[i])
        # Explore
        backtrack(candidates, target - candidates[i], i, path, result)
        # Unchoose (backtrack)
        path.pop()
    
    return result


# ============ CONNECTED COMPONENTS ============

def number_of_components(n, edges):
    """
    Count connected components in undirected graph.
    """
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1
    
    return components


# Example problems:
# - Binary Tree Inorder Traversal
# - Permutations
# - Combination Sum
# - Number of Islands
# - Clone Graph

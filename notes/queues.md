# Queues

## Concept

A **queue** is a First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.

**Key characteristics:**
- FIFO behavior
- Enqueue (add) and Dequeue (remove) operations
- Used for BFS, scheduling, buffering
- Natural for level-order traversal

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |
| Search | O(n) |

---

## Space Complexity

- **O(n)** – To store n elements

---

## Common Patterns

### 1. Basic Queue Implementation
Using Python's deque for efficient O(1) operations.

```python
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.popleft()  # Dequeue - O(1) with deque
```

### 2. Level-Order Traversal (BFS)
Process elements level by level using a queue.

```python
# Example: BFS on tree
from collections import deque

def level_order(root):
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
```

### 3. Deque - Double-Ended Queue
Use deque for operations on both ends.

```python
# Example: Sliding window maximum using deque
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()  # Stores indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### 4. Queue for Shortest Path / BFS
Find shortest path in unweighted graphs.

```python
# Example: Shortest path in grid
from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = set([(0, 0)])
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return dist
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1
```

---

## Interview Tips

1. **Use deque** – Python's `collections.deque` is optimal for O(1) operations on both ends.
2. **BFS template** – Queues are essential for BFS; know the pattern.
3. **Level-order traversal** – Track the number of elements at each level.
4. **Shortest path** – BFS finds shortest path in unweighted graphs.
5. **Memory** – BFS can use significant memory for large graphs; consider DFS if space is limited.

---

## Common Mistakes

- ❌ Using list.pop(0) instead of deque (O(n) vs O(1))
- ❌ Not marking visited nodes, causing infinite loops
- ❌ Forgetting to process entire level in level-order traversal
- ❌ Off-by-one errors in window/sliding problems
- ❌ Not handling empty queue edge cases

---

## Key Takeaways

✅ **FIFO structure** – Perfect for processing order matters.  
✅ **BFS is fundamental** – Master queue-based BFS.  
✅ **Use deque** – Always use deque for efficiency.  
✅ **Level-order traversal** – Natural for trees and graphs.  
✅ **Shortest path** – BFS finds it in unweighted graphs.

---

**Related Problems:** Binary Tree Level Order Traversal, Number of Islands, Rotting Oranges, Walls and Gates, Serialize and Deserialize Binary Tree

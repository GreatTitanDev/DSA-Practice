# Prefix Sum

## Concept

A **prefix sum** array stores cumulative sums up to each index, enabling fast O(1) range sum queries.

**Why use it:**
- Fast range queries (O(1) after O(n) preprocessing)
- Solve subarray sum problems efficiently
- Avoid recalculating sums repeatedly

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Build prefix sum | O(n) |
| Range sum query | O(1) |
| Space | O(n) |

---

## Common Patterns

### 1. Build Prefix Sum Array
Precompute cumulative sums.

```python
# Example: Build prefix sum
def build_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

# Usage
arr = [1, 2, 3, 4, 5]
prefix = build_prefix_sum(arr)
# prefix = [0, 1, 3, 6, 10, 15]

# Range sum from index i to j (inclusive)
def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]
```

### 2. Subarray Sum Equals K
Find number of subarrays with sum equal to k.

```python
# Example: Subarray sum equals k
def subarray_sum(nums, k):
    prefix_sum = 0
    sum_count = {0: 1}  # Base case: sum 0 seen once
    result = 0
    
    for num in nums:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, we found valid subarrays
        if prefix_sum - k in sum_count:
            result += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return result

# Time: O(n), Space: O(n)
```

### 3. Maximum Subarray Sum
Find contiguous subarray with largest sum (Kadane's algorithm uses prefix concept).

```python
# Example: Maximum subarray sum
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### 4. Contiguous Array (Equal 0s and 1s)
Find longest contiguous subarray with equal 0s and 1s.

```python
# Example: Contiguous array with equal 0s and 1s
def find_max_length(nums):
    # Convert 0 -> -1, so equal count means sum = 0
    prefix_sum = 0
    first_occurrence = {0: -1}  # Base case
    max_len = 0
    
    for i in range(len(nums)):
        prefix_sum += 1 if nums[i] == 1 else -1
        
        if prefix_sum in first_occurrence:
            max_len = max(max_len, i - first_occurrence[prefix_sum])
        else:
            first_occurrence[prefix_sum] = i
    
    return max_len
```

### 5. 2D Prefix Sum (Matrix Range Sum)
Fast queries for rectangular regions in a 2D matrix.

```python
# Example: 2D prefix sum
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix = None
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix[i][j] = (matrix[i-1][j-1] +
                                    self.prefix[i-1][j] +
                                    self.prefix[i][j-1] -
                                    self.prefix[i-1][j-1])
    
    def sum_region(self, r1, c1, r2, c2):
        return (self.prefix[r2+1][c2+1] -
                self.prefix[r1][c2+1] -
                self.prefix[r2+1][c1] +
                self.prefix[r1][c1])
```

---

## Interview Tips

1. **Recognize the pattern** – Multiple range queries? Use prefix sum!
2. **Hash map for lookups** – Store prefix sums for O(1) lookup.
3. **Base case matters** – Initialize with 0 at index 0.
4. **Transform problem** – Sometimes you need to transform data (e.g., 0 -> -1).
5. **2D case** – Principle extends to 2D with inclusion-exclusion.

---

## Common Mistakes

- ❌ Off-by-one errors in building prefix sum
- ❌ Forgetting base case (0 at start)
- ❌ Incorrect range query formula
- ❌ Not handling negative numbers
- ❌ Confusing inclusive vs exclusive ranges

---

## Key Takeaways

✅ **O(1) range queries** – After O(n) preprocessing.  
✅ **Hash map optimization** – Store prefix sums for subarray problems.  
✅ **Prefix sum formula** – `range_sum(i, j) = prefix[j+1] - prefix[i]`  
✅ **Transform data** – Use tricks like 0 -> -1 for clever solutions.  
✅ **Extends to 2D** – Use inclusion-exclusion principle.

---

**Related Problems:** Range Sum Query, Subarray Sum Equals K, Maximum Subarray, Contiguous Array, 2D Range Sum Query

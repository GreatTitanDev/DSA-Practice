# Arrays

## Concept

An **array** is a contiguous block of memory storing elements of the same type, accessed via indices.

**Key characteristics:**
- Fixed size (in most languages; Python lists are dynamic)
- 0-indexed access
- Contiguous memory allocation
- Fast random access

---

## Time Complexity

| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Access | O(1) | O(1) | O(1) |
| Search | O(1) | O(n) | O(n) |
| Insert | O(1) | O(n) | O(n) |
| Delete | O(1) | O(n) | O(n) |

---

## Space Complexity

- **O(n)** – To store n elements

---

## Common Patterns

### 1. Two Pointer Technique
Used for problems where you iterate from both ends or meet in the middle.

```python
# Example: Reverse array in-place
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

### 2. Sliding Window
For finding subarrays with specific properties (max sum, min length, etc.).

```python
# Example: Max sum of k consecutive elements
def max_sum_window(arr, k):
    if len(arr) < k:
        return -1
    
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(len(arr) - k):
        current_sum = current_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### 3. Prefix Sum
Precompute cumulative sums for range queries.

```python
# Example: Build prefix sum array
arr = [1, 2, 3, 4, 5]
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Query range sum from index i to j
range_sum = prefix[j+1] - prefix[i]
```

### 4. Sorting and Searching
- Use built-in sort for quick solutions (O(n log n))
- Binary search for sorted arrays (O(log n))
- Hash maps for O(1) lookups

---

## Interview Tips

1. **Understand the constraint** – Is the array sorted? Are there negative numbers? Duplicates?
2. **In-place modification** – Some problems require O(1) space; consider modifying the array itself.
3. **Edge cases** – Empty arrays, single elements, duplicates.
4. **Multiple passes** – Sometimes one pass isn't enough; plan for multiple iterations.
5. **Precomputation** – Use prefix sums, frequency maps, or sorted copies if it helps.

---

## Common Mistakes

- ❌ Off-by-one errors (confusing 0-indexed and 1-indexed)
- ❌ Modifying array while iterating
- ❌ Not considering space complexity of auxiliary arrays
- ❌ Assuming array is sorted when it's not
- ❌ Not handling empty array edge cases

---

## Key Takeaways

✅ **Arrays are fundamental** – Master them first.  
✅ **Know the patterns** – Two pointers, sliding window, prefix sum.  
✅ **Optimize for space** – Try in-place solutions.  
✅ **Think about sorting** – It often simplifies problems.  
✅ **Use hash maps** – For O(1) lookups and frequency counting.

---

**Related Problems:** Two Sum, Remove Duplicates, Best Time to Buy and Sell Stock, Majority Element, Rotate Array

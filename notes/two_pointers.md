# Two Pointers

## Concept

The **two pointers** technique uses two references that traverse an array or linked list from different directions or speeds.

**When to use:**
- Finding pairs or triplets
- Removing/modifying elements in-place
- Detecting cycles
- Merging sorted structures

---

## Time Complexity

- **O(n)** – Single pass with two pointers
- Space: **O(1)** – No extra space for most problems

---

## Common Patterns

### 1. Opposite Direction
Start from both ends and move towards center.

```python
# Example: Reverse array in-place
def reverse(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
```

### 2. Same Direction (Slow & Fast)
Pointers move at different speeds for cycle detection or removing elements.

```python
# Example: Remove duplicates in-place
def remove_duplicates(nums):
    if len(nums) < 2:
        return len(nums)
    
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow
```

### 3. Meeting in Middle
Find a pair with a specific sum.

```python
# Example: Two sum (sorted array)
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]
```

### 4. Partition
Rearrange array to separate elements by condition.

```python
# Example: Sort colors (0, 1, 2)
def sort_colors(nums):
    left, mid, right = 0, 0, len(nums) - 1
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        else:
            mid += 1
```

### 5. Container with Most Water
Find the optimal pair by moving pointers strategically.

```python
# Example: Container with most water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        
        # Move the pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

---

## Interview Tips

1. **Ask if sorted** – Two pointers work best on sorted arrays.
2. **In-place modification** – Two pointers excel at this (O(1) space).
3. **Direction matters** – Choose appropriate pointer movements.
4. **Visualize the problem** – Draw arrays and pointer movements.
5. **Edge cases** – Single element, all same, empty array.

---

## Common Mistakes

- ❌ Moving both pointers in the same direction when they should diverge
- ❌ Not checking boundary conditions
- ❌ Comparing wrong elements
- ❌ Forgetting to handle case where pointers cross
- ❌ Off-by-one errors in pointer movements

---

## Key Takeaways

✅ **O(1) space** – Most efficient for in-place operations.  
✅ **Two passes often needed** – One pass to setup, one to solve.  
✅ **Opposite vs same direction** – Choose based on problem.  
✅ **Sorted arrays shine** – Two pointers work best here.  
✅ **Partition problems** – Think three pointers for complex partitioning.

---

**Related Problems:** Container With Most Water, Move Zeroes, Valid Palindrome, Sort Colors, Trapping Rain Water

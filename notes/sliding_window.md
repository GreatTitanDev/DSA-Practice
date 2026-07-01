# Sliding Window

## Concept

The **sliding window** technique maintains a window of elements and slides it across the array to find subarrays matching a condition.

**Types:**
- **Fixed window** – Window size is constant (e.g., max sum of k elements)
- **Variable window** – Window size changes (e.g., longest substring with unique chars)

---

## Time Complexity

- **O(n)** – Each element enters and exits the window once
- Space: **O(k)** – For hash map or auxiliary data structure

---

## Common Patterns

### 1. Fixed Window Size
Find optimal result in all fixed-size windows.

```python
# Example: Maximum sum of k consecutive elements
def max_sum_window(nums, k):
    if len(nums) < k:
        return 0
    
    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 2. Variable Window - Expand and Contract
Expand window to include more elements, contract when condition fails.

```python
# Example: Longest substring without repeating characters
def longest_substring_unique(s):
    char_index = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 3. Minimum Window Substring
Find smallest window containing all required characters.

```python
# Example: Minimum window substring
def min_window(s, t):
    if not s or not t:
        return ""
    
    required = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    formed = 0
    window_counts = {}
    left = 0
    min_len = float('inf')
    min_start = 0
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        while formed == len(required) and left <= right:
            char = s[left]
            
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""
```

### 4. Frequency-Based Sliding Window
Track character frequencies in window.

```python
# Example: Longest repeating character replacement
def character_replacement(s, k):
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # If replacements needed > k, shrink window
        max_freq = max(char_count.values())
        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

---

## Interview Tips

1. **Identify the window condition** – What makes a valid window?
2. **Two pointers** – Sliding window needs left and right pointers.
3. **Hash map for tracking** – Often need to track frequencies or positions.
4. **Expand/contract strategy** – Expand right, contract left when needed.
5. **Optimize gradually** – Start with brute force, then optimize.

---

## Common Mistakes

- ❌ Not handling empty strings or edge cases
- ❌ Incorrect window contraction logic
- ❌ Not resetting hash maps properly
- ❌ Confusing "contains at least one" vs "contains all"
- ❌ Off-by-one in window size calculations

---

## Key Takeaways

✅ **O(n) time** – Much better than nested loops.  
✅ **Two pointers** – Core to sliding window technique.  
✅ **Fixed vs variable** – Know which applies to your problem.  
✅ **Hash maps track state** – Use for frequencies or last seen positions.  
✅ **Expand then contract** – General pattern for variable windows.

---

**Related Problems:** Longest Substring Without Repeating Characters, Minimum Window Substring, Permutation in String, Longest Repeating Character Replacement, Max Consecutive Ones III

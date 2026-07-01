# Hash Maps (Dictionaries)

## Concept

A **hash map** (or hash table) is an unordered collection of key-value pairs, providing fast O(1) average lookup, insertion, and deletion.

**In Python:** Dictionaries are hash maps.

**Key characteristics:**
- Fast lookups (O(1) average case)
- Unordered storage
- Keys must be hashable (immutable)
- Great for counting and grouping

---

## Time Complexity

| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Lookup | O(1) | O(1) | O(n) |
| Insert | O(1) | O(1) | O(n) |
| Delete | O(1) | O(1) | O(n) |

**Note:** Worst case occurs with poor hash function / many collisions. Rarely happens in practice.

---

## Space Complexity

- **O(n)** – To store n key-value pairs

---

## Common Patterns

### 1. Frequency Counting
Count occurrences of elements for quick lookup.

```python
# Example: Find first unique character
def first_unique(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s:
        if freq[char] == 1:
            return char
    return -1
```

### 2. Grouping Elements
Group elements by some property.

```python
# Example: Group anagrams
def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))  # Anagrams have same sorted key
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
```

### 3. Two Sum Pattern
Find pairs that match a condition using hash map.

```python
# Example: Two sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return [-1, -1]
```

### 4. Using defaultdict
Simplify code with automatic default values.

```python
from collections import defaultdict

# Count occurrences
counter = defaultdict(int)
for item in items:
    counter[item] += 1

# Group items
groups = defaultdict(list)
for item, category in data:
    groups[category].append(item)
```

---

## Interview Tips

1. **Think about the hash key** – What makes sense to hash? (sorted string, tuple, integer?)
2. **Use Counter** – Python's `collections.Counter` is optimized for counting.
3. **Key collisions** – Understand how your language handles them (usually via chaining or open addressing).
4. **Memory tradeoff** – Hash maps use space to gain speed.
5. **Validate assumptions** – Ensure keys are hashable (lists can't be keys, tuples can).

---

## Common Mistakes

- ❌ Assuming dictionaries are ordered (they are in Python 3.7+, but not guaranteed in older versions)
- ❌ Forgetting that lists/dicts can't be keys
- ❌ Not initializing default values when needed
- ❌ Modifying dict while iterating over it
- ❌ Confusing `key in dict` with `value in dict`

---

## Key Takeaways

✅ **O(1) lookups** – Hash maps are your go-to for fast access.  
✅ **Frequency counting** – Always consider if a hash map helps.  
✅ **Grouping** – Hash maps naturally group related items.  
✅ **Two passes** – Often need one pass to build map, another to query.  
✅ **Use Counter** – Leverage Python's built-in optimized counter.

---

**Related Problems:** Valid Anagram, Group Anagrams, Intersection of Two Arrays, Happy Number, Majority Element

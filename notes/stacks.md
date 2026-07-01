# Stacks

## Concept

A **stack** is a Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (the top).

**Key characteristics:**
- LIFO behavior
- Push (add) and Pop (remove) operations
- Simple, efficient implementation
- Great for problems involving nested structures or reversal

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

---

## Space Complexity

- **O(n)** – To store n elements

---

## Common Patterns

### 1. Valid Parentheses
Use a stack to match opening and closing brackets.

```python
# Example: Valid parentheses
def is_valid(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack
```

### 2. Next Greater Element
Find the next greater element for each element.

```python
# Example: Next greater element
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # Stores indices
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result
```

### 3. Monotonic Stack
Maintain a stack in decreasing/increasing order for optimization.

```python
# Example: Daily temperatures (find next warmer day)
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # Stores indices
    
    for i in range(len(temps)):
        while stack and temps[stack[-1]] < temps[i]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result
```

### 4. Stack to Implement Other Structures
Implement queues or other structures using stacks.

```python
# Example: Queue using two stacks
class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x):
        self.in_stack.append(x)
    
    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
```

---

## Interview Tips

1. **Recognize nesting problems** – Stacks are perfect for balanced parentheses, nested expressions.
2. **Think about reversal** – Stacks naturally reverse order.
3. **Monotonic stacks** – Powerful for "next" problems (next greater, next smaller).
4. **Stack vs recursion** – Recursion uses a call stack; sometimes explicit stack is cleaner.
5. **Edge cases** – Empty stack, single element, all same elements.

---

## Common Mistakes

- ❌ Accessing stack without checking if empty
- ❌ Confusing push/pop order
- ❌ Not handling edge cases (empty input)
- ❌ Inefficient nested loops when monotonic stack would help
- ❌ Forgetting to return proper value after operations

---

## Key Takeaways

✅ **LIFO structure** – Perfect for matching and reversal problems.  
✅ **Monotonic stacks** – Efficient for "next" element problems.  
✅ **Nested structures** – Stacks handle parentheses, XML, etc.  
✅ **Simple implementation** – Python lists work perfectly as stacks.  
✅ **O(1) operations** – Push and pop are constant time.

---

**Related Problems:** Valid Parentheses, Daily Temperatures, Next Greater Element, Trapping Rain Water, Minimum Stack

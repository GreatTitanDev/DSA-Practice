"""
Prefix Sum Template

Use for range sum queries, subarray problems.
Time Complexity: O(n) build, O(1) query
Space Complexity: O(n)
"""


# ============ 1D PREFIX SUM ============

def build_prefix_sum_1d(nums):
    """
    Build prefix sum array for fast range queries.
    prefix[i] = sum of nums[0] to nums[i-1]
    """
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix


def range_sum_query_1d(prefix, left, right):
    """
    Query range sum from index left to right (inclusive).
    Time: O(1)
    """
    return prefix[right + 1] - prefix[left]


# ============ SUBARRAY SUM EQUALS K ============

def subarray_sum_equals_k(nums, k):
    """
    Count number of subarrays with sum equal to k.
    Uses prefix sum + hash map for O(n) solution.
    """
    prefix_sum = 0
    sum_count = {0: 1}  # Base case: prefix sum 0 seen once
    result = 0
    
    for num in nums:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, we found valid subarrays
        if prefix_sum - k in sum_count:
            result += sum_count[prefix_sum - k]
        
        # Add current prefix sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return result


# ============ MAXIMUM SUBARRAY SUM (KADANE'S ALGORITHM) ============

def max_subarray_sum(nums):
    """
    Find contiguous subarray with largest sum.
    Kadane's algorithm using prefix concept.
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# ============ CONTIGUOUS ARRAY (EQUAL 0s AND 1s) ============

def find_max_length_equal_zeros_ones(nums):
    """
    Find longest contiguous subarray with equal 0s and 1s.
    Convert 0 -> -1, find longest subarray with sum 0.
    """
    prefix_sum = 0
    first_occurrence = {0: -1}  # Base case
    max_len = 0
    
    for i in range(len(nums)):
        # Convert 0 to -1
        prefix_sum += 1 if nums[i] == 1 else -1
        
        if prefix_sum in first_occurrence:
            max_len = max(max_len, i - first_occurrence[prefix_sum])
        else:
            first_occurrence[prefix_sum] = i
    
    return max_len


# ============ 2D PREFIX SUM ============

class NumMatrix2D:
    """
    2D matrix with fast range sum queries.
    Build: O(n*m), Query: O(1)
    """
    
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix = None
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build 2D prefix sum using inclusion-exclusion
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix[i][j] = (matrix[i-1][j-1] +
                                    self.prefix[i-1][j] +
                                    self.prefix[i][j-1] -
                                    self.prefix[i-1][j-1])
    
    def sum_region(self, r1, c1, r2, c2):
        """
        Query sum of rectangle from (r1,c1) to (r2,c2) inclusive.
        Formula: prefix[r2+1][c2+1] - prefix[r1][c2+1] 
                - prefix[r2+1][c1] + prefix[r1][c1]
        """
        return (self.prefix[r2+1][c2+1] -
                self.prefix[r1][c2+1] -
                self.prefix[r2+1][c1] +
                self.prefix[r1][c1])


# ============ PRODUCT OF ARRAY EXCEPT SELF ============

def product_except_self(nums):
    """
    For each index, return product of all other elements.
    Without division, O(n) time, O(1) space (excluding output).
    """
    n = len(nums)
    result = [1] * n
    
    # Prefix products: result[i] = product of all before index i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Suffix products: multiply by product of all after index i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


# ============ RANGE SUM WITH MODIFICATION ============

class PrefixSumWithUpdate:
    """
    Handle range sum queries with point updates.
    For simple cases, rebuild prefix sum.
    For many updates, use Fenwick Tree or Segment Tree.
    """
    
    def __init__(self, nums):
        self.nums = nums
        self.prefix = self._build_prefix()
    
    def _build_prefix(self):
        prefix = [0] * (len(self.nums) + 1)
        for i in range(len(self.nums)):
            prefix[i + 1] = prefix[i] + self.nums[i]
        return prefix
    
    def update(self, index, val):
        """Update value at index (simple O(n) rebuild)."""
        self.nums[index] = val
        self.prefix = self._build_prefix()
    
    def sum_range(self, left, right):
        """Query range sum."""
        return self.prefix[right + 1] - self.prefix[left]


# Example problems:
# - Range Sum Query 1D
# - Range Sum Query 2D
# - Subarray Sum Equals K
# - Maximum Subarray
# - Contiguous Array
# - Product of Array Except Self
# - Prefix and Suffix Search

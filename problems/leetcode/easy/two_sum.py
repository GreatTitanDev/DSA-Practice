"""
Two Sum - LeetCode Easy

Given an array of integers nums and an integer target, return the indices 
of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not 
use the same element twice.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Time Complexity: O(n)
Space Complexity: O(n) for hash map
"""


def two_sum(nums, target):
    """
    Find indices of two numbers that sum to target.
    
    Approach: Use hash map to store (value -> index)
    For each number, check if (target - number) exists in map.
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found


# Alternative approach (sorted + two pointers)
def two_sum_sorted(nums, target):
    """
    If we needed the actual values and array was sorted.
    This doesn't work for LeetCode Two Sum (which needs indices),
    but useful to know the pattern.
    """
    nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums_sorted) - 1
    
    while left < right:
        current_sum = nums_sorted[left][1] + nums_sorted[right][1]
        
        if current_sum == target:
            return [nums_sorted[left][0], nums_sorted[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


if __name__ == "__main__":
    # Test cases
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All test cases passed!")

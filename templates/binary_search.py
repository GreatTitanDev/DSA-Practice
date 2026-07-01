"""
Binary Search Template

Use this template for binary search problems on sorted arrays.
Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(nums, target):
    """
    Find target in sorted array.
    Returns index if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Search right
        else:
            right = mid - 1  # Search left
    
    return -1  # Not found


def binary_search_leftmost(nums, target):
    """
    Find leftmost (first) occurrence of target.
    Returns index of first target, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(nums, target):
    """
    Find rightmost (last) occurrence of target.
    Returns index of last target, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_insert_position(nums, target):
    """
    Find position where target should be inserted to keep array sorted.
    """
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


# Example problems:
# - Search in Sorted Array
# - First Bad Version
# - Search for a Range
# - Search in Rotated Sorted Array

"""
Container With Most Water - LeetCode Medium

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The max area is between indices 1 and 8 (8 and 7).

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_area(height):
    """
    Find maximum area container.
    
    Approach: Two pointers from both ends, move inward.
    Key insight: Moving the taller pointer inward can't increase area
    (limited by shorter line). Only moving shorter pointer has potential.
    
    Area = width * min(left_height, right_height)
    """
    left, right = 0, len(height) - 1
    max_area_val = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        
        # Update max
        max_area_val = max(max_area_val, area)
        
        # Move pointer pointing to shorter line inward
        # This is optimal: moving the taller pointer can only decrease area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area_val


# Brute force approach (for reference, don't use)
def max_area_brute_force(height):
    """
    Brute force: try all pairs.
    Time: O(n^2), Space: O(1)
    """
    max_area_val = 0
    
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height
            max_area_val = max(max_area_val, area)
    
    return max_area_val


if __name__ == "__main__":
    # Test cases
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([2, 3, 4]) == 4
    assert max_area([2, 3]) == 2
    assert max_area([1, 1]) == 1
    print("All test cases passed!")

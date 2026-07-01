"""
Sliding Window Template

Use for subarray/substring problems with fixed or variable window.
Time Complexity: O(n)
Space Complexity: O(k) for hash map, where k = window size
"""


# ============ FIXED WINDOW SIZE ============

def fixed_window(nums, k):
    """
    Find result over all fixed-size windows.
    Example: Maximum sum of k consecutive elements
    """
    if len(nums) < k:
        return None
    
    # Calculate initial window
    window = sum(nums[:k])
    result = window
    
    # Slide the window
    for i in range(len(nums) - k):
        # Remove leftmost, add new rightmost
        window = window - nums[i] + nums[i + k]
        result = max(result, window)
    
    return result


# ============ VARIABLE WINDOW - EXPAND & CONTRACT ============

def longest_substring_without_repeating(s):
    """
    Find longest substring without repeating characters.
    Uses: expand right, contract left when duplicate found
    """
    char_index = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        # If character exists in current window, move left pointer
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        # Update character's latest position
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len


def minimum_window_substring(s, t):
    """
    Find minimum window in s that contains all characters from t.
    Expand right until window is valid, then contract left to minimize.
    """
    if not s or not t:
        return ""
    
    # Build required character frequency
    required = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    # Track formed requirements
    formed = 0
    window_counts = {}
    left = 0
    min_len = float('inf')
    min_start = 0
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If character count matches required, increment formed
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        # Try to contract window from left
        while formed == len(required) and left <= right:
            char = s[left]
            
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove left character
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# ============ FREQUENCY-BASED SLIDING WINDOW ============

def character_replacement(s, k):
    """
    Find longest substring after at most k replacements.
    Keep most frequent character, replace others.
    """
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Add new character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # If characters to replace > k, shrink window
        max_freq = max(char_count.values()) if char_count else 0
        chars_to_replace = (right - left + 1) - max_freq
        
        while chars_to_replace > k:
            char_count[s[left]] -= 1
            left += 1
            max_freq = max(char_count.values()) if char_count else 0
            chars_to_replace = (right - left + 1) - max_freq
        
        max_len = max(max_len, right - left + 1)
    
    return max_len


# ============ PERMUTATION IN SUBSTRING ============

def permutation_in_string(s1, s2):
    """
    Check if s1 permutation is substring of s2.
    Use fixed-size window matching required characters.
    """
    if len(s1) > len(s2):
        return False
    
    # Required character counts
    required = {}
    for char in s1:
        required[char] = required.get(char, 0) + 1
    
    # Sliding window
    window = {}
    for i in range(len(s1)):
        char = s2[i]
        window[char] = window.get(char, 0) + 1
    
    if window == required:
        return True
    
    # Slide window
    for i in range(len(s1), len(s2)):
        # Add new character
        new_char = s2[i]
        window[new_char] = window.get(new_char, 0) + 1
        
        # Remove old character
        old_char = s2[i - len(s1)]
        window[old_char] -= 1
        if window[old_char] == 0:
            del window[old_char]
        
        if window == required:
            return True
    
    return False


# ============ TEMPLATE PATTERN ============

def sliding_window_template(array, condition_func):
    """
    Generic sliding window template.
    condition_func: determines when window is valid.
    """
    left = 0
    result = None
    window_data = {}  # Track data in current window
    
    for right in range(len(array)):
        # Expand: add right element
        element = array[right]
        window_data[element] = window_data.get(element, 0) + 1
        
        # Contract: shrink from left while condition holds
        while condition_func(window_data):
            left_element = array[left]
            window_data[left_element] -= 1
            if window_data[left_element] == 0:
                del window_data[left_element]
            left += 1
        
        # Process result
        window_size = right - left + 1
        if result is None or window_size < result:
            result = window_size
    
    return result


# Example problems:
# - Longest Substring Without Repeating Characters
# - Minimum Window Substring
# - Permutation in String
# - Longest Repeating Character Replacement
# - Max Consecutive Ones III
# - Minimum Size Subarray Sum
# - Sliding Window Maximum

def binary_search(array: list, target: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        if target < array[mid]:
            right = mid + 1
        else:
            left = mid - 1
            
    return -1

numbers = [12, 13, 15, 23, 26, 31, 35, 41]
print(binary_search(numbers, 23))
            

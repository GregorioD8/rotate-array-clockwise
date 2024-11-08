def rotate_array(arr, k):
    # Handle empty array and unnecessary rotations
    if not arr:
        return arr
    k = k % len(arr)
    if k == 0:
        return arr
    
    # Rotate the array by slicing
    return arr[-k:] + arr[:-k]


# Test cases
print(rotate_array([1, 2, 3, 4], 1))  # Expected output: [4, 1, 2, 3]
print(rotate_array([1, 2, 3], 2))     # Expected output: [2, 3, 1]
print(rotate_array([1, 2, 3], 3))     # Expected output: [1, 2, 3]
print(rotate_array([1, 2, 3, 4, 5], 0))  # Expected output: [1, 2, 3, 4, 5]
print(rotate_array([], 3))               # Expected output: []
print(rotate_array([1, 2, 3, 4], 4))     # Expected output: [1, 2, 3, 4]
print(rotate_array([1, 2, 3, 4, 5], 7))  # Expected output: [4, 5, 1, 2, 3]
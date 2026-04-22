def two_sum(nums, target):
    """
    Finds two indices that add up to the target using a Hash Map for O(n) speed.
    """
    prev_map = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

# Test Case
print(f"Indices: {two_sum([2, 7, 11, 15], 9)}") # Output: [0, 1]

# Complexity: Time O(n), Space O(n)

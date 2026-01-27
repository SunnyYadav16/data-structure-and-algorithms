"""
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements
in nums such that they add up to the target.

Each input will have exactly one solution, and the same element cannot be used twice.

Example 1
Input: nums = [1, 6, 2, 10, 3], target = 7
Output: [0, 1]
Explanation: nums[0] + nums[1] = 1 + 6 = 7

Example 2
Input: nums = [1, 3, 5, -7, 6, -3], target = 0
Output: [1, 5]
Explanation: nums[1] + nums[5] = 3 + (-3) = 0
"""

# BETTER SOLUTION
# TC - O(N)
# SC - O(N)
def two_sum_better(nums, target_val):
    n = len(nums)
    element_map = {}

    for i in range(n):
        remaining_val = target_val - nums[i]
        if remaining_val in element_map:
            return [element_map[remaining_val], i]
        else:
            element_map[nums[i]] = i

    return element_map


# OPTIMAL APPROACH
# TC - O(N) + O(N*logN)
# SC - O(N)
def two_sum_optimal(nums, target_val):
    n = len(nums)
    left = 0
    right = len(nums) - 1

    element_with_index = []
    for i in range(n):
        element_with_index.append([nums[i], i])

    element_with_index.sort(key= lambda x: x[0])

    while left < right:
        total = element_with_index[left][0] + element_with_index[right][0]
        if total < target_val:
            left += 1
        elif total > target_val:
            right -= 1
        else:
            return [element_with_index[left][1], element_with_index[right][1]]
    return -1


if __name__ == "__main__":
    input_arr = [1, 6, 2, 10, 3]
    target = 7
    # print(two_sum_better(input_arr, target))
    print(two_sum_optimal(input_arr, target))
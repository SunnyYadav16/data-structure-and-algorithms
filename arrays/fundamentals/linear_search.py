"""
Given an array of integers nums and an integer target, find the smallest index (0 based indexing)
where the target appears in the array. If the target is not found in the array, return -1.

Example 1
Input: nums = [2, 3, 4, 5, 3], target = 3
Output: 1
Explanation: The first occurence of 3 in nums is at index 1

Example 2
Input: nums = [2, -4, 4, 0, 10], target = 6
Output: -1
Explanation: The value 6 does not occur in the array, hence output is -1
"""


def linear_search(nums, target):
    for index, value in enumerate(nums):
        if value == target:
            return index

    return -1


if __name__ == "__main__":
    input_arr = [2,3,4,5,3]
    target_num = 6
    print(linear_search(input_arr, target_num))
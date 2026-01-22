"""
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [3, 4, 5, 6, 1, 2]
Explanation:
rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

Example 2
Input: nums = [3, 4, 1, 5, 3, -5], k = 8
Output: nums = [1, 5, 3, -5, 3, 4]
Explanation:
rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]
"""


# TC - O(N)
# SC - O(1)
def rotate_array(nums, k):
    n = len(nums)
    if k == n or k == 0:
        return nums

    split_index = k % n

    reverse_array(nums, 0, split_index-1)
    reverse_array(nums, split_index, n-1)
    reverse_array(nums, 0, n-1)
    return nums


def reverse_array(nums_arr, low, high):
    while low < high:
        nums_arr[low], nums_arr[high] = nums_arr[high], nums_arr[low]
        low += 1
        high -= 1

if __name__ == "__main__":
    input_arr =  [3, 4, 1, 5, 3, -5]
    k = 8
    print(rotate_array(input_arr, k))
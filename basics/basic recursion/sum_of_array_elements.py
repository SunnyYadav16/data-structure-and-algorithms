"""
Given an array nums, find the sum of elements of an array using recursion.

Example 1
Input : nums = [1, 2, 3]
Output : 6
Explanation : The sum of elements of an array is 1 + 2 + 3 => 6.

Example 2
Input : nums = [5, 8, 1]
Output : 14
Explanation : The sum of elements of an array is 5 + 8 + 1 => 14.

Example 3
Input : nums = [12, 9, 17]
Output: 38
"""


# TC - O(N)
def sum_of_array(arr):
    return calculate_sum(arr, 0)


def calculate_sum(nums, i):
    if i >= len(nums):
        return 0

    return nums[i] + calculate_sum(nums, i+1)


if __name__ == "__main__":
    input_arr = [10,2,30]

    print(sum_of_array(input_arr))
"""
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example 1
Input : nums = [1, 2, 3, 4, 5]
Output : true
Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2
Input : nums = [1, 2, 1, 4, 5]
Output : false
Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.
"""

def check_sorted_array(nums):
    return check_array(nums, 1, len(nums) - 1)

def check_array(nums, start, end):
    if start > end:
        return True
    if nums[start] < nums[start - 1]:
        return False

    return check_array(nums, start + 1, end)


if __name__ == "__main__":
    input_arr = [10,2,230]

    print(check_sorted_array(input_arr))
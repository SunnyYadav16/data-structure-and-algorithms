"""
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, modify the given array.

Example 1
Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
Explanation: Initially, nums = [1, 2, 3, 4, 5]. Rotating once to left -> nums = [2, 3, 4, 5, 1]

Example 2
Input: nums = [-1, 0, 3, 6]
Output: [0, 3, 6, -1]
Explanation: Initially, nums = [-1, 0, 3, 6]. Rotating once to left -> nums = [0, 3, 6, -1]
"""

# TC - O(N)
# SC - O(N)
def rotate_array_v2(nums):
    temp_arr = nums + nums
    nums = temp_arr[1: len(nums)+1]

    return nums


# TC - O(N)
# SC - O(1)
def rotate_array(nums):
    first_element = nums[0]
    n = len(nums)

    for i in range(1, n):
        nums[i-1] = nums[i]

    nums[n-1] = first_element
    return nums

if __name__ == "__main__":
    input_arr =  [1,2,3,4,5]
    print(rotate_array(input_arr))
    print(rotate_array_v2(input_arr))
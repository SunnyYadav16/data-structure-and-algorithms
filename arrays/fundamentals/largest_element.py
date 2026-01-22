"""
Given an array of integers nums, return the value of the largest element in the array

Example 1
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Example 2
Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99
"""

def largest_element(nums):
    max_val = float('-inf')

    for num in nums:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    input_arr =  [3, 3, 6, 1]
    print(largest_element(input_arr))
"""
Given an array of integers nums, return the second-largest element in the array.
If the second-largest element does not exist, return -1.

Example 1
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation: The largest value in nums is 8, the second largest is 7

Example 2
Input: nums = [10, 10, 10, 10, 10]
Output: -1
Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned
"""

def second_largest_element(nums):
    max_val = float('-inf')
    second_max = float('-inf')

    for val in nums:
        if val > max_val:
            second_max = max_val
            max_val = val
        elif second_max < val < max_val:
            second_max = val

    return -1 if second_max == float('-inf') else second_max


if __name__ == "__main__":
    input_arr =  [1000,-10000]
    print(second_largest_element(input_arr))
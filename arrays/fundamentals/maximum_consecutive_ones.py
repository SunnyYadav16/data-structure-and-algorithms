"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.

Example 1
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
Output: 3
Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2
Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
Output: 0
Explanation: No 1s are present in nums, thus we return 0
"""

def maximum_consecutive_ones(nums):
    max_val = 0
    counter = 0

    for i in nums:
        if i == 1:
            counter += 1
            max_val = max(max_val, counter)
        else:
            counter = 0

    return max_val




if __name__ == "__main__":
    input_arr =  [1, 1, 0, 0, 1, 1, 1, 0]
    print(maximum_consecutive_ones(input_arr))
"""
Given an integer array nums, return a list of all the leaders in the array.

A leader in an array is an element whose value is strictly greater than all elements to its right in the given array.
The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the
nums array.

Example 1
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]
Explanation: 2 is the rightmost element, 3 is the largest element in the index range [3, 5],
5 is the largest element in the index range [2, 5]

Example 2
Input: nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]
Explanation: -5 is the rightmost element, -4 is the largest element in the index range [4, 5],
1 is the largest element in the index range [3, 5], and 5 is the largest element in the range [2, 5]
"""

# TC - O(N)
# SC - O(1)
def leader_in_array(nums):
    n = len(nums)
    max_val = nums[-1]
    temp_arr = [max_val]

    for i in range(n-2, -1, -1):
        if nums[i] > max_val:
            max_val = nums[i]
            temp_arr.append(nums[i])

    temp_arr.reverse()
    return temp_arr

if __name__ == "__main__":
    input_arr =   [1, 2, 5, 3, 1, 2]
    print(leader_in_array(input_arr))

"""
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements
present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15
Explanation: The subarray from index 0 to index 4 has the largest sum = 15

Example 2
Input: nums = [-2, -3, -7, -2, -10, -4]
Output: -2
Explanation: The element on index 0 or index 3 make up the largest sum when taken as a subarray
"""

# BETTER SOLUTION
# TC - O(N^2)
# SC - O(1)
def kadane_algo(nums):
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]

            max_sum = max(total, max_sum)

    return max_sum

# OPTIMAL SOLUTION
# TC - O(N)
# SC - O(1)
def kadane_algo_optimal(nums):
    n = len(nums)
    max_val = float('-inf')
    total = 0

    for i in range(n):
        if total < 0:
            total = 0
        total += nums[i]

        max_val = max(max_val, total)

    return max_val if max_val > 0 else []

# OPTIMAL SOLUTION - BUT ALSO PRINT THE SUBARRAY WITH MAX VALUE
# TC - O(N)
# SC - O(1)
def kadane_algo_optimal_subarray(nums):
    n = len(nums)
    max_val = float('-inf')
    total = 0
    start = 0
    ans_start = ans_end = -1

    for i in range(n):
        if total == 0:
            start = i

        total += nums[i]
        if total < 0:
            total = 0

        if total > max_val:
            max_val = total
            ans_start = start
            ans_end = i

    for i in range(ans_start, ans_end + 1):
        print(nums[i], end=" ")
    print()
    return max_val if max_val > 0 else []


if __name__ == "__main__":
    input_arr = [2, 3, 5, -2, 7, -4]
    print(kadane_algo(input_arr))
    print(kadane_algo_optimal(input_arr))
    print(kadane_algo_optimal_subarray(input_arr))
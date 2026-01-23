"""
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive),
return the only number missing from the array within this range.

Example 1
Input: nums = [0, 2, 3, 1, 4]
Output: 5
Explanation: nums contain 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2
Input: nums = [0, 1, 2, 4, 5, 6]
Output: 3
Explanation: nums contain 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]
"""

# OPTIMAL SOLUTION 1
# TC - O(N)
# SC - O(1)
def missing_number(nums):
    n = len(nums)
    arr_total = sum(nums)
    number_sum = (n * (n+1)) // 2

    return number_sum - arr_total


# OPTIMAL SOLUTION 2 (Slightly better than the above approach when the numbers are large enough)
# TC - O(N)
# SC - O(1)
def missing_number_xor(nums):
    n = len(nums)
    xor_1, xor_2 = 0, 0

    for i in range(0, n):
        xor_2 ^= nums[i]
        xor_1 ^= (i + 1)

    return xor_1 ^ xor_2


if __name__ == "__main__":
    input_arr =  [0, 2, 3, 1, 4]
    print(missing_number(input_arr))
    print(missing_number_xor(input_arr))
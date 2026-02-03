"""
Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array,
except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.

Example 1
Input: nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation: 1 appears two times in the array, and 2 is missing from nums

Example 2
Input: nums = [1, 2, 3, 6, 7, 5, 7]
Output: [7, 4]
Explanation: 7 appears two times in the array, and 4 is missing from nums.
"""
from collections import defaultdict


# BRUTE FORCE SOLUTION
# TC - O(N ^ 2)
# SC - O(1)
def repeating_missing_number(nums):
    n = len(nums)
    missing_number = repeating_number= -1

    for i in range(1, n +1):
        counter = 0
        for j in range(n):
            if nums[j] == i:
                counter += 1

        if counter == 2:
            repeating_number = i

        elif counter == 0:
            missing_number = i

        if repeating_number != -1 and missing_number != -1:
            break

    return [repeating_number, missing_number]


# BETTER SOLUTION
# TC - O(2N)
# SC - O(N)
def repeating_missing_number_better(nums):
    n = len(nums)
    hash_list = [0] * (n + 1)
    missing_number = repeating_number = -1

    for num in nums:
        hash_list[num] += 1

    for i in range(1, n+1):
        if hash_list[i] == 2:
            repeating_number = i
        elif hash_list[i] == 0:
            missing_number = i

        if repeating_number != -1 and missing_number != -1:
            break

    return [repeating_number, missing_number]


# OPTIMAL SOLUTION 1
# IDEA IS TO USE MATHS FORMULAS TO CALCULATE THE REPEATING AND MISSING NUMBER
# arr - [3,1,2,5,4,6,7,5], n = 8
# SN = Sum of first 'n' natural numbers = (n*(n+1)) // 2 => 36
# S2N-Sum of square first 'n' natural numbers = (n* (n+1) * (2n+1) // 6 => 204
# S = Sum of elements of the array => 33
# S2 = Sum of square of elements of the array => 165
# val1 = S - SN => -3
# val2 = S2 - S2N => -39
# val2 = val2 // val1 => 13
# (Repeating) x = (val1 + val2) // 2 => 5
# (Missing) y = x - val1 => 8
# TC - O(N)
# SC - O(1)
def repeating_missing_number_optimal(nums):
    n = len(nums)
    sum_of_numbers = 0
    sum_of_square_of_numbers = 0
    sum_of_n_numbers = (n * (n + 1)) // 2
    sum_of_square_of_n_numbers = (n * (n + 1) * (2 * n + 1)) // 6

    for i in range(n):
        sum_of_numbers += nums[i]
        sum_of_square_of_numbers += nums[i] * nums[i]

    value_1 = sum_of_numbers - sum_of_n_numbers # x - y
    value_2 = sum_of_square_of_numbers - sum_of_square_of_n_numbers # x^2 - y^2
    value_2 = value_2 // value_1 # x + y
    x = (value_1 + value_2) // 2 # repeating number
    y = x - value_1 # missing number

    return [x, y]


if __name__ == "__main__":
    input_arr = [3, 5, 4, 1, 1]
    print(repeating_missing_number(input_arr))
    print(repeating_missing_number_better(input_arr))
    print(repeating_missing_number_optimal(input_arr))
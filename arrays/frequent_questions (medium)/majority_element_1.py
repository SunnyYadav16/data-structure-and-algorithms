"""
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array.
The array is guaranteed to have a majority element.

Example 1
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7
Explanation: The number 7 appears 5 times in the 9 sized array

Example 2
Input: nums = [1, 1, 1, 2, 1, 2]
Output: 1
Explanation: The number 1 appears 4 times in the 6 sized array
"""


# BETTER APPROACH
# TC - O(N)
# SC - O(N)
from collections import  Counter

def majority_element_better(nums):
    c = Counter(nums)
    n = len(nums) // 2

    for key, value in c.items():
        if value > n:
            return key
    return None


# OPTIMAL APPROACH (BOYER-MOORE's ALGORITHM)
# The majority element always dominates other numbers, so it cancels out non-majority elements when counting.
# Even if the count resets, the majority element eventually overtakes.
# TC - O(N)
# SC - O(1)
def majority_element_optimal(nums):
    n = len(nums)
    majority_element, majority_count = nums[0], 1

    for i in range(1, n):
        if majority_count == 0:
            majority_element = nums[i]
            majority_count = 1
        elif majority_element == nums[i]:
            majority_count += 1
        else:
            majority_count -= 1

    total_count_of_majority_element = 0

    for i in range(n):
        if nums[i] == majority_element:
            total_count_of_majority_element += 1

    if total_count_of_majority_element > (n // 2):
        return majority_element


if __name__ == "__main__":
    input_arr =  [-1, -1, -1, -1]
    print(majority_element_better(input_arr))
    print(majority_element_optimal(input_arr))
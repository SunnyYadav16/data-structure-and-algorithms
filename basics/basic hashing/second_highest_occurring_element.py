"""
Given an array of n integers, find the second most frequent element in it.

If there are multiple elements that appear second most frequent times, find the smallest of them.
If second most frequent element does not exist return -1.

Example 1
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 2
Explanation:
The number 2 appears the second most (2 times) and number 3 appears the most(3 times).

Example 2
Input: arr = [4, 4, 5, 5, 6, 7]
Output: 6
Explanation:
Both 6 and 7 appear second most times, but 6 is smaller.
"""
from collections import Counter


def find_second_highest_occurring_element(nums, n):
    hash_map = Counter(nums)

    highest_element_key = -1
    highest_element_val = 0
    second_element_key = -1
    second_element_val = 0

    for key, value in hash_map.items():
        if value > highest_element_val:
            second_element_key, second_element_val = highest_element_key, highest_element_val
            highest_element_key, highest_element_val = key, value
        elif value == highest_element_val:
            highest_element_key = min(highest_element_key, key)
        elif value > second_element_val:
            second_element_key, second_element_val = key, value
        elif value == second_element_val:
            second_element_key = min(second_element_key, key)

    return second_element_key


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3]
    print(find_second_highest_occurring_element(arr, len(arr)))
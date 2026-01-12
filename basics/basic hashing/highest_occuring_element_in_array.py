"""
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the
maximum number of times.
If there are multiple elements that appear a maximum number of times, find the smallest of them.

Example 1
Input: nums = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Example 2
Input: nums = [4, 4, 5, 5, 6]
Output: 4
Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.
"""

from collections import Counter


def find_highest_occurring_element(arr, n):
    hash_map = Counter(arr)
    # for i in arr:
    #     if i not in hash_map:
    #         hash_map[i] = 1
    #     else:
    #         hash_map[i] += 1

    highest_occuring_ele = float('-inf')
    highest_occuring_val = float('-inf')

    for key, value in hash_map.items():
        if value > highest_occuring_val:
            highest_occuring_ele = key
            highest_occuring_val = value
        elif value == highest_occuring_val:
            highest_occuring_ele = min(highest_occuring_ele, key)

    return highest_occuring_ele


if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5, 5]
    print(find_highest_occurring_element(arr, len(arr)))
"""
Given an array of n integers, find the sum of frequencies of the highest occurring number and the lowest occurring number.

Example 1
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 4
Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

Example 2
Input: arr = [4, 4, 5, 5, 6]
Output: 3
Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.
"""

from collections import Counter

def calculate_sum_of_highest_lowest_freq(nums):
    freq_map = Counter(nums)

    highest_freq = max(freq_map.values())
    lowest_freq = min(freq_map.values())

    return highest_freq + lowest_freq


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3]
    print(calculate_sum_of_highest_lowest_freq(arr))
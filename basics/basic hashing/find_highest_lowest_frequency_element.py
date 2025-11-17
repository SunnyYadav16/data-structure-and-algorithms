"""
Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
"""

def find_highest_lowest_element(arr, n):
    map_counter = {}
    for key in range(n):
        if arr[key] in map_counter:
            map_counter[arr[key]] += 1
        else:
            map_counter[arr[key]] = 1

    highest_freq_element = float('-inf')
    highest_freq_count = float('-inf')
    lowest_freq_element = float('-inf')
    lowest_freq_count = float('inf')

    for key, value in map_counter.items():
        if value > highest_freq_count:
            highest_freq_element = key
            highest_freq_count = value
        if value < lowest_freq_count:
            lowest_freq_element = key
            lowest_freq_count = value

    return highest_freq_element, lowest_freq_element


if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]
    print(find_highest_lowest_element(arr, len(arr)))

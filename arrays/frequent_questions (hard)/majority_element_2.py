"""
Given an integer array nums of size n. Return all elements that appear more than n/3 times in the array.
The output can be returned in any order.

Example 1
Input: nums = [1, 2, 1, 1, 3, 2]
Output: [1]
Explanation: Here, n / 3 = 6 / 3 = 2.
Therefore, the elements appearing 3 or more times is : [1]

Example 2
Input: nums = [1, 2, 1, 1, 3, 2, 2]
Output: [1, 2]
Explanation: Here, n / 3 = 7 / 3 = 2.
Therefore, the elements appearing 3 or more times is : [1, 2]
"""
from collections import Counter, defaultdict


def majority_element(nums):
    n = len(nums)
    element_count = Counter(nums)
    majority_ele = n//3
    my_list = []

    for key, value in element_count.items():
        if value > majority_ele:
            my_list.append(key)

    my_list.sort()
    return my_list


# BETTER SOLUTION
#  If n = 9, then n/3 = 3. To be a majority element, you need at least 4 occurrences.
#  If you had three different elements appearing 4 times each, you would need 4 + 4 + 4 = 12 slots,
#  but you only have 9.
# TC - O(N * logN), where N is size of the given array
# SC - O(N) for using a map data structure
def majority_element_better(nums):
    n = len(nums)
    minimum_occurrence = (n // 3) + 1
    result_list = []
    mpp = defaultdict(int)

    for i in range(n):
        mpp[nums[i]] += 1
        if mpp[nums[i]] == minimum_occurrence:
            result_list.append(nums[i])

        if len(result_list) == 2:
            break
    return result_list


# OPTIMAL SOLUTION
# TC - O(N)
# SC - O(1)
def majority_element_optimal(nums):
    n = len(nums)
    counter1 = counter2 = 0
    element1 = element2 = float('-inf')
    result_list = []

    for i in range(n):
        if counter1 == 0 and nums[i] != element2:
            counter1 += 1
            element1 = nums[i]
        elif counter2 == 0 and nums[i] != element1:
            counter2 += 1
            element2 = nums[i]
        elif nums[i] == element1:
            counter1 += 1
        elif nums[i] == element2:
            counter2 += 1
        else:
            counter1 -= 1
            counter2 -= 1

    total_count_of_majority_element1 = 0
    total_count_of_majority_element2 = 0
    min_occurrence = n // 3 + 1

    for i in range(n):
        if nums[i] == element1:
            total_count_of_majority_element1 += 1
        elif nums[i] == element2:
            total_count_of_majority_element2 += 1

    if total_count_of_majority_element1 > min_occurrence:
        result_list.append(element1)

    if total_count_of_majority_element2 > min_occurrence:
        result_list.append(element2)

    result_list.sort()
    return result_list


if __name__ == "__main__":
    input_arr = [1, 2, 1, 1, 3, 2, 2]
    print(majority_element(input_arr))
    print(majority_element_better(input_arr))
    print(majority_element_optimal(input_arr))
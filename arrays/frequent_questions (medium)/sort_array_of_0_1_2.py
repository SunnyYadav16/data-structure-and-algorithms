"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.

Example 1
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Example 2
Input: nums = [0, 0, 1, 1, 1]
Output: [0, 0, 1, 1, 1]
Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos
"""

# BETTER SOLUTION
# TC - O(2N)
# SC - O(1)
def sort_array(nums):
    n = len(nums)
    counter_zero = counter_one = counter_two = 0

    for i in range(n):
        if nums[i] == 0:
            counter_zero += 1
        elif nums[i] == 1:
            counter_one += 1
        else:
            counter_two += 1

    for i in range(0, n-counter_one-counter_two):
        nums[i] = 0
    for i in range(counter_zero, counter_zero+counter_one):
        nums[i] = 1
    for i in range(counter_zero+counter_one, n):
        nums[i] = 2
    return nums


# OPTIMAL SOLUTION
# TC - O()
# SC - O()
def sort_array_optimal(nums):
    n = len(nums)
    low, mid, high = 0, 0, n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

if __name__ == "__main__":
    input_arr = [1, 0, 2, 1, 0]
    # print(sort_array(input_arr))
    print(sort_array_optimal(input_arr))
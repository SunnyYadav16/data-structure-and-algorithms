"""
Given an integer array nums. Return the number of reverse pairs in the array.
An index pair (i, j) is called a reverse pair if:
0 <= i < j < nums.length
nums[i] > 2 * nums[j]

Example 1
Input: nums = [6, 4, 1, 2, 7]
Output: 3
Explanation: The reverse pairs are:
(0, 2): nums[0] = 6, nums[2] = 1, 6 > 2 * 1
(0, 3): nums[0] = 6, nums[3] = 2, 6 > 2 * 2
(1, 2): nums[1] = 4, nums[2] = 1, 4 > 2 * 1

Example 2
Input: nums = [5, 4, 4, 3, 3]
Output: 0
Explanation: No pairs satisfy both the conditions.
"""

# OPTIMAL SOLUTION - UPDATED MERGE SORT
# TC - O(2N * log N)
# SC - O(N)
def merge(nums, low, mid, high):
    left = low
    right = mid + 1
    temp_arr = []

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp_arr.append(nums[left])
            left += 1
        else:
            temp_arr.append(nums[right])
            right += 1

    while left <= mid:
        temp_arr.append(nums[left])
        left += 1

    while right <= high:
        temp_arr.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp_arr[i - low]

    return nums

def count_pairs(nums, low, mid, high):
    right = mid + 1
    counter = 0

    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        counter += right - (mid + 1)

    return counter

def merge_sort(nums, low, high):
    counter = 0
    if low >= high:
        return counter

    mid = (low + high) // 2
    counter += merge_sort(nums, low, mid)
    counter += merge_sort(nums, mid + 1, high)
    counter += count_pairs(nums, low, mid, high)
    merge(nums, low, mid, high)

    return counter

def reverse_pairs(nums):
    n = len(nums)
    return merge_sort(nums, 0, n-1)

if __name__ == "__main__":
    input_arr = [6, 4, 1, 2, 7]
    print(reverse_pairs(input_arr))
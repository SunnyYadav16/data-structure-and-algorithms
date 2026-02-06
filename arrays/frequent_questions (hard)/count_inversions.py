"""
Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.

Example 1
Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5
Explanation:
The responsible indexes are:
nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

Example 2
Input: nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation: nums is sorted, hence no inversions present.
"""

# BRUTE FORCE SOLUTION
# TC - O(N^2)
# SC - O(1)
def count_inversions(nums):
    n = len(nums)

    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j] and i < j:
                counter += 1

    return counter


# OPTIMAL SOLUTION - USING MERGE SORT
# TC - O(N log N)
# SC - O(N)
def merge_sort(nums, low, high):
    counter = 0
    if low >= high:
        return counter
    mid = (low + high) // 2
    counter += merge_sort(nums, low, mid)
    counter += merge_sort(nums, mid+1, high)
    counter += merge(nums, low, mid, high)
    return counter

def merge(nums, low, mid, high):
    left = low
    right = mid+1
    temp_arr = []

    count = 0
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp_arr.append(nums[left])
            left += 1
        else:
            temp_arr.append(nums[right])
            count += mid - left + 1
            right += 1

    while left <= mid:
        temp_arr.append(nums[left])
        left += 1

    while right <= high:
        temp_arr.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp_arr[i - low]

    return count

def count_inversions_optimal(nums):
    n = len(nums)
    return merge_sort(nums, 0, n-1)


if __name__ == "__main__":
    input_arr = [2, 3, 7, 1, 3, 5]
    print(count_inversions(input_arr))
    print(count_inversions_optimal(input_arr))
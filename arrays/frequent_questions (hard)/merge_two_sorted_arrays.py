"""
Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
Merge both the arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.

Example 1
Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
Output: [-5, -3, -2, 1, 4, 5, 8]
Explanation: The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1
            and [-3, 1, 8] are from nums2

Example 2
Input: nums1 = [0, 2, 7, 8], nums2 = [-7, -3, -1]
Output: [-7, -3, -1, 0, 2, 7, 8]
Explanation: The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1
            and [-7, -3, -1] are from nums2
"""

# BRUTE FORCE SOLUTION
# TC - O(N+M) + O(N+m)
# SC - O(N + M)
def merge_sorted_arrays(nums1, m, nums2, n):
    left = right = 0
    temp_arr = []

    while left < m and right < n:
        if nums1[left] < nums2[right]:
            temp_arr.append(nums1[left])
            left += 1
        else:
            temp_arr.append(nums2[right])
            right += 1

    while left < m:
        temp_arr.append(nums1[left])
        left += 1

    while right < n:
        temp_arr.append(nums2[right])
        right += 1

    for i in range(m+n):
        nums1[i] = temp_arr[i]

    return nums1


# OPTIMAL SOLUTION
# TC -
# SC -
def merge_sorted_arrays_optimal(nums1, m, nums2, n):
    ptr_i = m-1
    ptr_j = n-1
    index = m + n - 1

    while ptr_i >= 0 and ptr_j >= 0:
        if nums1[ptr_i] >= nums2[ptr_j]:
            nums1[index] = nums1[ptr_i]
            index -= 1
            ptr_i -= 1
        else:
            nums1[index] = nums2[ptr_j]
            index -= 1
            ptr_j -= 1

    return nums1

if __name__ == "__main__":
    input_arr1 = [-5, -2, 4, 5, 0, 0, 0]
    input_arr2 = [-3, 1, 8]
    # print(merge_sorted_arrays(input_arr1, 4, input_arr2, len(input_arr2)))
    print(merge_sorted_arrays_optimal(input_arr1, 4, input_arr2, len(input_arr2)))

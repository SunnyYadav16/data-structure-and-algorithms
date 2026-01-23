"""
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either the first array,
the second array, or both.

Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]
Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2
Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
Output: [1, 3, 4, 5, 6, 7, 8, 9]
Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
"""

def union_of_arrays(nums1, nums2):
    union_arr = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            if not union_arr or union_arr[-1] != nums1[i]:
                union_arr.append(nums1[i])
            i += 1
        else:
            if not union_arr or union_arr[-1] != nums2[j]:
                union_arr.append(nums2[j])
            j += 1

    while i < len(nums1):
        if not union_arr or union_arr[-1] != nums1[i]:
            union_arr.append(nums1[i])
        i += 1

    while j < len(nums2):
        if not union_arr or union_arr[-1] != nums2[j]:
            union_arr.append(nums2[j])
        j += 1

    return union_arr


if __name__ == "__main__":
    input_arr =  [3, 4, 6, 7, 9, 9]
    input_arr_2 = [1, 5, 7, 8, 8]
    print(union_of_arrays(input_arr, input_arr_2))

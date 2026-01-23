"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note: that elements beyond the length of the original array are not written. Do the above modifications to the
input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

# WITHOUT USING OTHER ARRAY (IN-PLACE)
def duplicate_zeroes(nums):
    counter = 0
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            counter += 1

    if counter == 0 or n == counter:
        return nums

    i = n - 1
    j = n - 1 + counter

    while i >= 0 and j >= 0:
        if j < n:
            nums[j] = nums[i]
        j -= 1

        if nums[i] == 0:
            if j < n:
                nums[j] = nums[i]
            j -= 1
        i -= 1

    return nums

# USING ANOTHER ARRAY TO COPY ELEMENTS
def duplicate_zeroes_v2(nums):
    n = len(nums)
    temp = [0] * n
    i, j = 0, 0

    while i < n and j < n:
        if nums[i] != 0:
            temp[j] = nums[i]
            j += 1
        else:
            j += 2
        i += 1

    for i in range(len(nums)):
        nums[i] = temp[i]

    return nums


if __name__ == "__main__":
    input_arr =  [1, 2, 3]
    print(duplicate_zeroes(input_arr))
    print(duplicate_zeroes_v2(input_arr))
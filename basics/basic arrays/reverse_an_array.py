"""
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Example 1
Input: n=5, arr = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Example 2
Input: n=6, arr = [1,2,1,1,5,1]
Output: [1,5,1,1,2,1]
Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].
"""

def reverse_arr(arr, n):
    start = 0
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

if __name__ == "__main__":
    number_arr = [1,2,3,4,5,6]
    print(reverse_arr(number_arr, len(number_arr)))
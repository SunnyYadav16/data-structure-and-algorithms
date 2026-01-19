"""
Problem Statement: Given an array of size n, sort the array using Merge Sort.

Example 1:
Input : N=7,arr[]={3,2,8,5,1,4,23}
Output : {1,2,3,4,5,8,23}
Explanation : Given array is sorted in non-decreasing order.

Example 2:
Input : N=5, arr[]={4,2,1,6,7}
Output : {1,2,4,6,7}
Explanation : Given array is sorted in non-decreasing order.
"""

# TC -  O(N * log base2 N) (log base 2 is because each time we are dividing the array in half)
def merge_sort(arr, low, high):
    if low == high: return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge_arr(arr, low, mid, high)

    return arr


def merge_arr(arr, low, mid, high):
    temp_arr = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left += 1
        else:
            temp_arr.append((arr[right]))
            right += 1

    while left <= mid:
        temp_arr.append(arr[left])
        left += 1

    while right <= high:
        temp_arr.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp_arr[i - low]

    return arr


if __name__ == "__main__":
    my_arr = [7,2,4,3,1,9,8,5,6,10,0]
    print(merge_sort(my_arr, 0, len(my_arr) - 1))
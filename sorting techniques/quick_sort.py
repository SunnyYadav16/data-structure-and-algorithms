"""
Problem Statement: Given an array of n integers, sort the array using the Quicksort method.

Examples
Input: N = 5, Arr[] = {4,1,7,9,3}
Output: {1, 3, 4, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 3, 4, 7, 9

Input: N = 8, Arr[] = {4,6,2,5,7,9,1,3}
Output: {1, 2, 3, 4, 5, 6, 7, 9}
Explanation: After sorting the array in ascending order it becomes 1, 2, 3, 4, 5, 6, 7, 9
"""

def quick_sort(arr, low, high):
    if low >= high: return

    partition_index = partition_func(arr, low, high)
    quick_sort(arr, low, partition_index - 1)
    quick_sort(arr, partition_index + 1, high)

    return arr


def partition_func(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low - 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


if __name__ == "__main__":
    my_arr = [7,2,4,3,1,9,8,5,6,10,0]
    print(quick_sort(my_arr, 0, len(my_arr) - 1))
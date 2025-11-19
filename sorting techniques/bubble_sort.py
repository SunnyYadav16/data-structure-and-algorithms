"""
Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52


Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
"""

def bubble_sort(arr):
    n = len(arr)

    did_swap = 0
    for i in range(n-1, 0, -1):
        for j in range(0 , i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap += 1

        if did_swap == 0:
            break
    return arr


if __name__ == "__main__":
    my_arr = [7,2,4,3,1,9,8,5,6,10,0]
    print(bubble_sort(my_arr))
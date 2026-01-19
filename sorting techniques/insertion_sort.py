"""
Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation:
After sorting the array is: 9,13,20,24,46,52


Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1,2,3,4,5
"""

# TC - O(N^2)
# Best case if array already sorted so while loop is never executed -  O(N)
def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


if __name__ == "__main__":
    my_arr = [7,2,4,3,1,9,8,5,6,10,0]
    print(insertion_sort(my_arr))
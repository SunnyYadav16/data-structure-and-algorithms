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

# LOOPING FROM END OF LIST (MOST EFFICIENT)
# TC - O(N^2)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        did_swap = False
        for j in range(0 , i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = True

        if not did_swap:
            break
    return arr


# LOOPING FROM START OF LIST
# TC - O(N^2)
def bubble_sort_v2(nums):
    n = len(nums)
    did_swap = 0
    for i in range(n-1):
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                did_swap +=1

        if did_swap == 0:
            break

    return nums


# USING WHILE LOOP
# TC - O(N^2)
def bubble_sort_v3(nums):
    n = len(nums)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                nums[i], nums[i+1] = nums[i+1], nums[i]

        if is_sorted:
            break

    return nums

if __name__ == "__main__":
    my_arr = [-44,48,-40,-38,-29,-5,-2,-7,-42,-16,-7,-40,14,-22,7]
    print(bubble_sort(my_arr))
    print(bubble_sort_v2(my_arr))
    print(bubble_sort_v3(my_arr))
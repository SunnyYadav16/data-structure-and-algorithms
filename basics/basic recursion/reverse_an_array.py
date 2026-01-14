"""
Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples:

Example 1:
Input: N = 5, input_str[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position,
            the second element occupies the fourth position and so on.

Example 2:
Input: N=6 input_str[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position,
            the second element occupies the fourth position and so on.
"""

# Normal recursive function
def recursive_func(my_arr, start, end):
    if start < end:
        my_arr[start], my_arr[end] = my_arr[end], my_arr[start]
        recursive_func(my_arr, start+1, end-1)

# Better approach with one variable
def recursive_func_with_single_var(index, my_arr, n):
    if index >= n/2:
        return
    my_arr[index], my_arr[n-index-1] = my_arr[n-index-1], my_arr[index]
    recursive_func_with_single_var(index+1, my_arr, n)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    recursive_func(arr, 0, len(arr) - 1)
    print(arr)

    recursive_func_with_single_var(0, arr, len(arr))
    print(arr)


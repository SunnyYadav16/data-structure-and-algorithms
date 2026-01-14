"""
Given an array input_str of size n, the task is to find the sum of all the elements in the array.

Example 1
Input: n=5, input_str = [1,2,3,4,5]
Output: 15
Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Example 2
Input: n=6, input_str = [1,2,1,1,5,1]
Output: 11
Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11
"""

# USING BUILT IN METHOD
def calculate_sum(arr, n):
    return sum(arr)

def calculate_sum_loop(arr, n):
    total = 0
    for i in range(n):
        total += arr[i]

    return total


if __name__ == "__main__":
    number_arr = [1,2,1,1,5,1]
    print(calculate_sum(number_arr, len(number_arr)))
    print(calculate_sum_loop(number_arr, len(number_arr)))
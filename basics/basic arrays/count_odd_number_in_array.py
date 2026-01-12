"""
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Example 1
Input: n=5, array = [1,2,3,4,5]
Output: 3
Explanation: The three odd elements are (1,3,5).

Example 2
Input: n=6, array = [1,2,1,1,5,1]
Output: 5
Explanation: The five odd elements are one 5 and four 1's.
"""

# Using Built in method
def find_odd(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            counter += 1
    return counter


if __name__ == "__main__":
    number_arr = [1,2,1,1,5,1]
    print(find_odd(number_arr))
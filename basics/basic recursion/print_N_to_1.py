"""
Problem Description: Given an integer N, write a program to print numbers from N to 1.

Examples
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1
Explanation: This is the base case.
"""


def recursive_func(n, end):
    if n < end:
        return
    print(n, end=" ")

    recursive_func(n-1, end)

if __name__ == "__main__":
    n = 5
    recursive_func(n, 1)

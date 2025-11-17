"""
Problem Description: Given an integer N, write a program to print numbers from N to 1 using backtracking.

Examples
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.

Input: N = 1
Output: 1
Explanation: This is the base case.
"""


def recursive_func(i, n):
    if i > n:
        return
    recursive_func(i + 1, n)
    print(i, end=" ")

if __name__ == "__main__":
    n = 5
    recursive_func(1, n)

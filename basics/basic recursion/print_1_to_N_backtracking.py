""""
Problem Description: Given an integer N, write a program to print numbers from 1 to N using backtracking.

Examples
Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.

Input: N = 1
Output: 1
Explanation: This is the base case.
"""

def recursive_func(i):
    if i < 1:
        return

    recursive_func(i-1)
    print(i, end=" ")

if __name__ == "__main__":
    n = 5
    recursive_func(n)


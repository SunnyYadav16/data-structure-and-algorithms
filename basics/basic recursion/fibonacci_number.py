"""
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
"""

def recursive_func(n):
    if n <= 1:
        return n
    if n == 2:
        return 1

    return recursive_func(n-1) + recursive_func(n-2)

if __name__ == "__main__":
    number = 5
    print(recursive_func(number))

"""
Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Ashish Ashish Ashish
Explanation: Name is printed 3 times.

Input: N = 1
Output: Ashish
Explanation: Name is printed once.
"""

def recursive_func(number):

    if number == 0:
        return
    print("Sunny", end=" ")
    recursive_func(number-1)


if __name__ == "__main__":
    n = 5
    recursive_func(n)
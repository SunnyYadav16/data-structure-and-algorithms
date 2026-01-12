"""
Problem Statement: Given a number X, print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it.
More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number.

Examples
Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1
"""

def loop_func(n):
    if n == 0 or n == 1:
        return 1

    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact


def recursive_func(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_func(n-1)


if __name__ == "__main__":
    n = 4
    loop_answer = loop_func(n)
    print(loop_answer)
    rec_answer = recursive_func(n)
    print(rec_answer)
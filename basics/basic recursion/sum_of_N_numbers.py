"""
Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Examples:

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
"""

# PARAMETERIZED PATTERN
def parameterized_func(i, sum):
    if i < 1:
        print(sum)
        return

    parameterized_func(i - 1, sum + i)


# FUNCTIONAL PATTERN
def recursive_func(n):
    if n == 0:
        return 0
    return n + recursive_func(n-1)


if __name__ == "__main__":
    n = 5

    parameterized_func(n, 0)

    func_answer = recursive_func(n)
    print(func_answer)
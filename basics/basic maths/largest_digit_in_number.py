"""
You are given an integer n. Return the largest digit present in the number.

Example 1
Input: n = 25
Output: 5
Explanation: The largest digit in 25 is 5.

Example 2
Input: n = 99
Output: 9
Explanation: The largest digit in 99 is 9.
"""


def largest_digit(num):
    if num == 0:
        return 0
    max_digit = float('-inf')

    while num > 0:
        digit = num % 10
        max_digit = max(max_digit, digit)
        num //= 10

    return max_digit


if __name__ == "__main__":
    number = int(input())
    print(largest_digit(number))
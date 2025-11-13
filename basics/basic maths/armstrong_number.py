"""
Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power
of the number of digits.

Examples
    Example 1:
    Input:N = 153
    Output:True
    Explanation: 1**3+5**3+3**3 = 1 + 125 + 27 = 153

    Example 2:
    Input:N = 371
    Output: True
    Explanation: 3**3+7**3+1**3 = 27 + 343 + 1 = 371
"""
import math

number = int(input())
original_number = number
digit_sum = 0
digit_count = int(math.log10(number) + 1)

while number > 0:
    remainder = number % 10
    digit_sum += remainder ** digit_count
    number //= 10

print(digit_sum == original_number)
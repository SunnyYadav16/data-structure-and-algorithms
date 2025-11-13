"""
Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward.
For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

Examples
    Example 1:
    Input:N = 4554
    Output:Palindrome Number
    Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number

    Example 2:
    Input:N = 7789
    Output: Not Palindrome
    Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome
"""

# BRUTE FORCE
number = int(input())

print(str(number) == str(number)[::-1])


# OPTIMAL APPROACH
number = int(input())
original_number = number
rev_result = 0

while number > 0:
    remainder = number % 10
    rev_result = rev_result * 10 + remainder
    number //= 10

print(original_number == rev_result)

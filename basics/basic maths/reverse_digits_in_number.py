"""
Problem Statement: Given a positive integer N return the reverse of the given number.

Note: If a number has trailing zeros, then its reverse will not include them.
For e.g., reverse of 10400 will be 401 instead of 00401.

Examples
    Example 1:
    Input:N = 12345
    Output:54321
    Explanation: The reverse of 12345 is 54321.

    Example 2:
    Input:N = 7789
    Output: 9877
    Explanation: The reverse of number 7789 is 9877.
"""

# BRUTE FORCE
number = int(input())
reversed_string = ""

while number > 0:
    remainder = number % 10
    reversed_string += str(remainder)
    number = number // 10

print(int(reversed_string))



# OPTIMAL APPROACH
number = int(input())
reversed_num = 0

while number > 0:
    remainder = number % 10
    reversed_num = reversed_num * 10 + remainder
    number = number // 10

print(reversed_num)
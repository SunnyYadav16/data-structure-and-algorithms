"""
Problem Statement: Given an integer N, return the number of digits in N.

Examples
    Example 1:
    Input:N = 12345
    Output:5
    Explanation:  The number 12345 has 5 digits.

    Example 2:
    Input:N = 7789
    Output: 4
    Explanation: The number 7789 has 4 digits.
"""

# BRUTE FORCE Approach 1
number = int(input())
print(len(str(number)))



# BRUTE FORCE Approach 2
number = int(input())
digit_count = 0

while number > 0:
    digit_count += 1
    number //= 10

print(digit_count)


# OPTIMAL APPROACH

import math

# The expression int(math.log10(n) + 1) calculates the number of digits in 'n' and casts it to an integer.
# Adding 1 to the result accounts for the case when 'n' is a power of 10, ensuring that the count is correct.
# Finally, the result is cast to an integer to ensure it is rounded down to the nearest whole number.
# Return the count of digits in 'n'.

number = int(input())
cnt = int(math.log10(number) + 1)
print(cnt)
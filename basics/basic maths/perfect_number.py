"""
You are given an integer n. You need to check if the number is a perfect number or not.
Return true if it is a perfect number, otherwise, return false.

A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

Example 1
Input: n = 6
Output: true
Explanation: Proper divisors of 6 are 1, 2, 3. 1 + 2 + 3 = 6.

Example 2
Input: n = 4
Output: false
Explanation: Proper divisors of 4 are 1, 2. 1 + 2 = 3.
"""
import math


# BRUTE FORCE - O(n)
def perfect_number(num):
    factor_sum = 0
    for i in range(1, num):
        if num % i ==0:
            factor_sum += i

    return factor_sum == num


# OPTIMAL - O(sqrt(n))
def optimal_perfect_number(num):

    if num == 1:
        return False

    original_num = num
    sqrt_num = int(math.sqrt(num))
    factor_sum = 0
    for i in range(1, sqrt_num+1):
        if num % i == 0:
            factor_sum += i

            # Add the counterpart divisor if it's
            # different from i and if it is not n itself
            if i != num // i and num != num // i:
                factor_sum += num//i

    return factor_sum == original_num


if __name__ == "__main__":
    number = int(input())
    print(optimal_perfect_number(number))
    print(perfect_number(number))
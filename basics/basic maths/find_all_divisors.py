"""
Problem Statement: Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder.
In other words, if N is divisible by another integer without any remainder, then that integer is
considered a divisor of N.

Examples
Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.
"""

# BRUTE FORCE - O(N)
def find_divisor(num):
    div_list = []
    for i in range(1, num+1):
        if num % i == 0:
            div_list.append(i)

    return div_list


# OPTIMAL APPROACH - O(sqrt(N) + O(log k * k)
def find_divisor_optimal(num):
    divisor_list = []

    for i in range(1, int(num ** 0.5) + 1):
        if number % i == 0:
            divisor_list.append(i)
            if number // i != i:
                divisor_list.append(int(number // i))

    divisor_list.sort()
    return divisor_list


if __name__ == "__main__":
    number = int(input())
    print(find_divisor(number))
    print(find_divisor_optimal(number))
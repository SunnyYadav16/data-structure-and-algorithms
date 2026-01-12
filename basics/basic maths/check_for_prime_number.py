"""
Problem Statement: Given an integer N, check whether it is prime or not.

A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

Examples
    Example 1:
    Input:N = 2
    Output:True
    Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).

    Example 2:
    Input:N = 10
    Output: False
    Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.
"""
import math

def check_prime(num):
    if num < 2:
        return False
    sqrt_num = int(math.sqrt(num))

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False

    return True

if __name__ == "__main__":
    number = int(input())
    print(check_prime(number))


"""
You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive).
Return the number of prime numbers in the range.

A prime number is a number which has no divisors except, 1 and itself.

Example 1
Input: n = 6
Output: 3
Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

Example 2
Input: n = 10
Output: 4
Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, 7.
"""


# BRUTE FORCE - O(N * SQRT(N))
import math

def count_prime_number(num):
    counter = 0
    for i in range(1, num + 1):
        if check_prime(i):
            counter += 1

    return counter

def check_prime(num):
    if num < 2:
        return False
    sqrt_num = int(math.sqrt(num))

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False
    return True



# SIEVE OF ERATOSTHENES
# OPTIMAL SOLUTION - O(N log (log N))
def count_primes(num):
    if num < 2:
        return 0
    prime_arr = [True] * (num + 1)
    prime_arr[0] = prime_arr[1] = False

    for i in range(2, int(num ** 0.5) + 1):
        if prime_arr[i]:
            for j in range(i * i, num + 1, i):
                prime_arr[j] = False

    return sum(prime_arr)


if __name__ == "__main__":
    number = int(input())
    print(count_primes(number))
    print(count_prime_number(number))

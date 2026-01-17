"""
Given an integer num, return true if it is prime otherwise false.

A prime number is a number that is divisible only by 1 and itself.

Example 1
Input : num = 5
Output : true
Explanation : The factors of 5 are 1 and 5 only.
So it satisfies the prime number condition.

Example 2
Input : num = 15
Output : false
Explanation : The factors of 15 are 1, 3, 5, 15 only.
As the number has factors other than 1 and itself, So it is not a prime number.
"""

def check_prime(num):
    def checker(num, i):
        if num < 2:
            return False

        if num % i == 0:
            return False
        
        return checker(num, i+1, (num ** 0.5) + 1)

    checker(num, 2)
    return



if __name__ == "__main__":
    number = int(input())
    print(check_prime(number))
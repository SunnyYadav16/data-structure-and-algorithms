"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1
Input : num = 529
Output : 7
Explanation : In first iteration the digits sum will be = 5 + 2 + 9 => 16
In second iteration the digits sum will be 1 + 6 => 7.
Now single digit is remaining , so we return it.

Example 2
Input : num = 101
Output : 2
Explanation : In first iteration the digits sum will be = 1 + 0 + 1 => 2
Now single digit is remaining , so we return it.
"""

def add_digits(num):
    if num < 10:
        return num
    digits_sum = sum_of_digits(num)

    return add_digits(digits_sum)


def sum_of_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_of_digits(num // 10)


if __name__ == "__main__":
    input_num = 3064

    print(add_digits(input_num))
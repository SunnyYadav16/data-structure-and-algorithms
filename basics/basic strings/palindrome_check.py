"""
You are given a string s. Return true if the string is palindrome, otherwise false.

A string is called palindrome if it reads the same forward and backward.

Example 1
Input : s = "hannah"
Output : true
Explanation :
The given string when read backward is -> "hannah", which is the same as when read forward. Hence, the answer is true.

Example 2
Input : s = "aabbaaa"
Output : false
Explanation :
The given string when read backward is -> "aaabbaa", which is different from when read forward. Hence, the answer is false.
"""

def palindrome_check(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    input_str = "hannah"
    print(palindrome_check(input_str))
"""
Problem Statement: "Given a string, check if the string is palindrome or not."
A string is said to be palindrome if the reverse of the string is the same as the string.

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string
"""

# Normal recursive function
def recursive_func(my_str, start, end):
    if start <= end and my_str[start] == my_str[end]:
        recursive_func(my_str, start+1, end-1)
        return "Palindrome"
    return "Not Palindrome"


# Better approach with one variable
def recursive_func_with_single_var(my_str, index, n):
    if index >= n/2:
        return "Palindrome"
    if my_str[index] != my_str[n-index-1]:
        return "Not Palindrome"
    return recursive_func_with_single_var(my_str, index+1, n)


if __name__ == "__main__":
    my_str = "ABCDCBA"
    print(recursive_func(my_str, 0, len(my_str) - 1))
    print(recursive_func_with_single_var(my_str, 0, len(my_str)))
"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1
Input : s = "abcde" , goal = "cdeab"
Output : true
Explanation :
After performing 2 shifts we can achieve the goal string from string s.
After first shift the string s is => bcdea
After second shift the string s is => cdeab.

Example 2
Input : s = "abcde" , goal = "adeac"
Output : false
Explanation :
Any number of shift operations cannot convert string s to string goal.
"""

# BRUTE FORCE - O(N^2)
def rotate_str(s, goal):
    n = len(s)
    list_s = list(s)
    for i in range(1, n+1):
        first_char = list_s[0]
        j = 1
        while j < n:
            list_s[j - 1] = list_s[j]
            j += 1
        list_s[j - 1] = first_char

        if "".join(list_s) == goal:
            return True

    return False



# OPTIMAL APPROACH - O(N)
def rotate_str_optimal(s, goal):
    if len(s) != len(goal):
        return False

    doubled_str = s + s
    return goal in doubled_str



if __name__ == "__main__":
    input_str_s = "abcde"
    input_str_t = "adeac"
    print(rotate_str(input_str_s, input_str_t))
    print(rotate_str_optimal(input_str_s, input_str_t))




"""
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string)
that is a substring of the given string s.

The number returned should not have leading zero's. But the given input string may have leading zero.
(If no odd number is found, then return empty string.)

Example 1
Input : s = "5347"
Output : "5347"
Explanation :
The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
So the largest among all the possible odd numbers for given string is 5347.

Example 2
Input : s = "0214638"
Output : "21463"
Explanation :
The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.
We cannot include 021463 as the number contains leading zero.
So largest odd number in given string is 21463.
"""

# BRUTE FORCE - O(N^2)
# THIS IS A GOOD SOLUTION BUT WILL GIVE TLE FOR LARGE CASES
def find_largest_odd(s):
    max_element = -1
    new_str = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            new_str += s[j]
            if int(new_str) % 2 != 0:
                max_element = max(max_element, int(new_str))
        new_str = ""

    return str(max_element) if max_element != -1 else ""



# OPTIMAL SOLUTION - O(N)
def find_largest_odd_optimal(s):
    j = -1

    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 1:
            j = i
            break

    if j == -1:
        return ""

    # THIS FOLLOWING LOOP CODE CAN BE REMOVED AS WELL.
    # IN PYTHON WE CAN USE THE lstrip('0') TO REMOVE THE LEADING ZEROES
    # AND DIRECTLY RETURN THE STRING. THAT WOULD BE JUST
    # return s[: j+1].lstrip('0')
    i = 0
    while i < len(s):
        if int(s[i]) != 0:
            break
        i += 1

    return s[i: j+1]


# OPTIMAL + CONCISE SOLUTION - O(N)
def find_largest_optimal_concise(s):
    n = len(s)

    for i in range(n - 1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[: i + 1].lstrip('0')

    return ""



if __name__ == "__main__":
    input_str = "0214638"
    print(find_largest_odd(input_str))
    print(find_largest_odd_optimal(input_str))
    print(find_largest_optimal_concise(input_str))
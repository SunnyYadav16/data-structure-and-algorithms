"""
Given a string, the task is to reverse it. The string is represented by an array of characters s.
Perform the reversal in place with O(1) extra memory.

Note: no need to return anything, modify the given list.

Example 1
Input : s = ["h", "e" ,"l" ,"l" ,"o"]
Output : ["o", "l", "l", "e", "h"]
Explanation :
The given string is s = "hello" and after reversing it becomes s = "olleh".

Example 2
Input : s = ["b", "y" ,"e" ]
Output : ["e", "y", "b"]
Explanation :
The given string is s = "bye" and after reversing it becomes s = "eyb".
"""

def reverse_string(str_arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
        left += 1
        right -= 1

    return str_arr


if __name__ == "__main__":
    arr = ["h", "e" ,"l" ,"l" ,"o"]
    print(reverse_string(arr))
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1
Input : s = "anagram" , t = "nagaram"
Output : true
Explanation :
We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

Example 2
Input : s = "dog" , t = "cat"
Output : false
Explanation :
We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.
"""
from collections import Counter


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    # mapS = Counter(s)
    #
    # for char_t in t:
    #     if char_t not in mapS or mapS[char_t] == 0:
    #         return False
    #     mapS[char_t] -= 1
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    input_str_s = "eat"
    input_str_t = "tea"
    print(valid_anagram(input_str_s, input_str_t))
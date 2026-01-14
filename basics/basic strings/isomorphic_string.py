"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1
Input : s = "egg" , t = "add"
Output : true
Explanation :
The 'e' in string s can be replaced with 'a' of string t.
The 'g' in string s can be replaced with 'd' of t.
Hence all characters in s can be replaced to get t.

Example 2
Input : s = "apple" , t = "bbnbm"
Output : false
Explanation :
Strings are matched index by index.
At index 0, 'a' maps to 'b'.
At index 1, 'p' also maps to 'b'.
This is invalid because two different characters (a and p) cannot map to the same character (b) in a one-to-one mapping.
Therefore, no valid mapping exists and the output is false.
"""

def isomorphic_check(s, t):
    if len(s) != len(t):
        return False

    hashST, hashTS = {}, {}

    for char_s, char_t in zip(s, t):

        if (char_s in hashST and hashST[char_s] != char_t) or (char_t in hashTS and hashTS[char_t] != char_s):
            return  False

        hashST[char_s] = char_t
        hashTS[char_t] = char_s

    return True

if __name__ == "__main__":
    input_str_s = "apple"
    input_str_t = "bbnbm"
    print(isomorphic_check(input_str_s, input_str_t))
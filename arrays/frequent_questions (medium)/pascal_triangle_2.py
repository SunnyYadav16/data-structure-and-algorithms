"""
Given an integer r, return all the values in the rth row (1-indexed) in Pascal's Triangle in correct order.

In Pascal's triangle:
The first row has one element with a value of 1.
Each row has one more element in it than its previous row.
The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

Example 1
Input: r = 4
Output: [1, 3, 3, 1]
Explanation:
The Pascal's Triangle is as follows:
1
1 1
1 2 1
1 3 3 1
....
Thus the 4th row is [1, 3, 3, 1]

Example 2
Input: r = 5
Output: [1, 4, 6, 4, 1]
Explanation:
The Pascal's Triangle is as follows:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
....
Thus the 5th row is [1, 4, 6, 4, 1]
"""

# TC - O(R), where R is the row number
# SC - O(1)
def pascal_triangle(row):

    def calculate_nCr(r):
        res = 1
        temp_arr = [res]
        for i in range(1, r):
            res *= (r - i)
            res //= i
            temp_arr.append(res)

        return temp_arr

    return calculate_nCr(row)


if __name__ == "__main__":
    input_r = 4
    print(pascal_triangle(input_r))

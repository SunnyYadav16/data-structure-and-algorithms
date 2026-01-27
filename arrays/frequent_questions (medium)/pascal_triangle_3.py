"""
Given an integer n, return the first n (1-Indexed) rows of Pascal's triangle.
Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]

In Pascal's triangle:
The first row has one element with a value of 1.
Each row has one more element in it than its previous row.
The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

Example 1
Input: n = 4
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
Explanation: The Pascal's Triangle is as follows:
1
1 1
1 2 1
1 3 3 1
1st Row has its value set to 1.
All other cells take their value as the sum of the values directly above them

Example 2
Input: n = 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
Explanation: The Pascal's Triangle is as follows:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1st Row has its value set to 1.
All other cells take their value as the sum of the values directly above them
"""

# TC - O(N^2), generating each row takes linear time relative to its size, and there are N rows,
#               leading to a total time complexity of O(N2).
# SC - O(N^2), storing the entire Pascal's Triangle requires space proportional to the sum of the
#               first N natural numbers, resulting in O(N2) space complexity.
def pascal_triangle(n):

    output_arr = []
    def calculate_nCr(r):
        res = 1
        temp_arr = [res]
        for i in range(1, r):
            res *= (r - i)
            res //= i
            temp_arr.append(res)

        return temp_arr

    for i in range(1, n+1):
        output_arr.append(calculate_nCr(i))

    return output_arr

if __name__ == "__main__":
    input_n = 4
    print(pascal_triangle(input_n))
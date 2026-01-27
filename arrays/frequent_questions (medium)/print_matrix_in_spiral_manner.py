"""
Given an M * N matrix, print the elements in a clockwise spiral manner.
Return an array with the elements in the order of their appearance when printed in a spiral manner.

Example 1
Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Explanation: The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

Example 2
Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
Output: [1, 2, 3, 4, 8, 7, 6, 5]
Explanation: The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

Example 3
Input: matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
Output: [1, 2, 4, 6, 8, 7, 5, 3]
"""

def print_in_spiral(matrix):
    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])
    top = left = 0
    bottom = no_of_rows - 1
    right = no_of_columns - 1
    res = []

    while top <= bottom and left <= right:
        # print all elements in top row (left -> right)
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1

        # print all elements in last column (top -> bottom)
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom: # This condition is used to prevent printing if there is only one row
            # print all elements in the last row (right -> left)
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right: # This condition is used to prevent printing if left is not less than right
            # print all elements in the first columns (bottom -> top)
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


if __name__ == "__main__":
    input_arr =  [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
    print(print_in_spiral(input_arr))
"""
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.

The rotation must be done in place, meaning the input 2D matrix must be modified directly.

Example 1
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Example 2
Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
"""


# GOOD SOLUTION - WON'T WORK IF ASKED TO SOLVE THE ARRAY IN-PLACE
def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    output_arr = []

    for i in range(1, cols + 1):
        temp_arr = []
        while rows > 0:
            temp_arr.append(matrix[rows-1][i-1])
            rows -= 1

        rows = len(matrix)
        output_arr.append(temp_arr)

    return output_arr

# TC - O(N^2) +O(N^2)
# SC - O(1)
def rotate_matrix_optimal(matrix):
    # Transpose
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse
    for i in range(n):
        matrix[i].reverse()

    return matrix

if __name__ == "__main__":
    input_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(rotate_matrix(input_arr))
    print(rotate_matrix_optimal(input_arr))
"""
Given an integer array nums. Find the subarray with the largest product, and return the product of the elements
present in that subarray. A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input: nums = [4, 5, 3, 7, 1, 2]
Output: 840
Explanation: The largest product is given by the whole array itself

Example 2
Input: nums = [-5, 0, -2]
Output: 0
Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].
"""

# BETTER SOLUTION
# TC - O(N ^ 2)
# SC - O(1)
def max_product_subarray(nums):
    n = len(nums)
    max_prod = float('-inf')

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            max_prod = max(prod, max_prod)

    return max_prod


# OPTIMAL SOLUTION
# TC - O(N)
# SC - O(1)
def max_product_subarray_optimal(nums):
    n = len(nums)
    prefix = suffix = 1
    max_prod = float('-inf')

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n-i-1]

        max_prod = max(max_prod, max(prefix, suffix))

    return max_prod

if __name__ == "__main__":
    input_arr = [4, 5, 3, 7, 1, 2]
    print(max_product_subarray(input_arr))
    print(max_product_subarray_optimal(input_arr))
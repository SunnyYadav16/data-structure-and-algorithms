"""
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets.
The output and the triplets can be returned in any order.

Example 1
Input: nums = [2, -2, 0, 3, -3, 5]
Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
Explanation:
nums[1] + nums[2] + nums[0] = 0
nums[4] + nums[1] + nums[5] = 0
nums[4] + nums[2] + nums[3] = 0

Example 2
Input: nums = [2, -1, -1, 3, -1]
Output: [[-1, -1, 2]]
Explanation:
nums[1] + nums[2] + nums[0] = 0
Note that we have used two -1s as they are separate elements with different indexes
But we have not used the -1 at index 4 as that would create a duplicate triplet
"""

# BETTER SOLUTION
# TC - O(N2 x log(no. of unique triplets)), where N is size of the array.
# Inserting triplets into the set takes O(log(no. of unique triplets)) time complexity
# SC - O(2 x no. of the unique triplets) + O(N)
def three_sum(nums):
    n = len(nums)
    triplet_set = set()

    for i in range(n):
        hash_set = set()
        for j in range(i+1, n):
            remaining_val = -(nums[i] + nums[j])
            if remaining_val in hash_set:
                three_sum_triplet = [nums[i], nums[j], remaining_val]
                three_sum_triplet.sort()
                triplet_set.add(tuple(three_sum_triplet))
            hash_set.add(nums[j])

    ans = [list(triplet) for triplet in triplet_set]

    return ans


# OPTIMAL SOLUTION
# TC - O(NlogN)+O(N^2)
# SC - O(1)
def three_sum_optimal(nums):
    n = len(nums)
    nums.sort()
    result_set = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]: continue
        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result_set.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]: j += 1
                while j < k and nums[k] == nums[k + 1]: k -= 1

    return result_set


if __name__ == "__main__":
    input_arr = [2, -1, -1, 3, -1]
    print(three_sum(input_arr))
    print(three_sum_optimal(input_arr))
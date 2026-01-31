"""
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.

Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets.
The output and the quadruplets can be returned in any order.

Example 1
Input: nums = [1, -2, 3, 5, 7, 9], target = 7
Output: [[-2, 1, 3, 5]]
Explanation: nums[1] + nums[0] + nums[2] + nums[3] = 7

Example 2
Input: nums = [7, -7, 1, 2, 14, 3], target = 9
Output: []
Explanation: No quadruplets are present which add upto 9
"""

# BETTER SOLUTION
# TC - O(N^3 x log(M))
# SC - O(2 x no. of the quadruplets)+O(N)
def four_sum(nums, target):
    n = len(nums)
    quad_set = set()

    for i in range(n):
        for j in range(i+ 1, n):
            hash_set = set()
            for k in range(j + 1, n):
                remaining_val = target - (nums[i] + nums[j] + nums[k])
                if remaining_val in hash_set:
                    temp = [nums[i], nums[j], nums[k], remaining_val]
                    temp.sort()
                    quad_set.add(tuple(temp))

                hash_set.add(nums[k])

    ans = [list(t) for t in quad_set]
    return ans


# OPTIMAL SOLUTION
# TC - O(N^3)
# SC - O(no. of quadruplets), this space is only used to store the answer.
# No extra space is used to solve this problem. So, from that perspective, space complexity can be written as O(1).
def four_sum_optimal(nums, target):
    n = len(nums)
    output_list = []
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                else:
                    output_list.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]: k += 1
                    while k < l and nums[l] == nums[l + 1]: l -= 1

    return output_list


if __name__ == "__main__":
    input_arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target_val = 9
    # print(four_sum(input_arr, target_val))
    print(four_sum_optimal(input_arr, target_val))
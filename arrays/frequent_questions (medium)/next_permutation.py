"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation
of that array is the permutation that follows it in the sorted order.

If such an arrangement is not possible (i.e., the array is the last permutation), then rearrange it to the
lowest possible order (i.e., sorted in ascending order).

You must rearrange the numbers in-place and use only constant extra memory.

Example 1
Input: nums = [1,2,3]
Output: [1,3,2]
Explanation: The next permutation of [1,2,3] is [1,3,2].

Example 2
Input: nums = [3,2,1]
Output: [1,2,3]
Explanation: [3,2,1] is the last permutation. So we return the first: [1,2,3].
"""


# OPTIMAL SOLUTION
# TC - O()
# SC - O()

# 1. Longer prefix match (a[i] < a[i+1])
# 2. Find the element that is greater than the current element A, but the smallest one from the right side, so that
#    you stay close
# 3. Place the remaining array in sorted order

def next_permutation(nums):
    n = len(nums)
    index = -1

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            index = i
            break

    if index == -1:
        nums.reverse()
        return nums

    for i in range(n-1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index+1:] = reversed(nums[index+1:])

    return nums

if __name__ == "__main__":
    input_arr = [2, 1, 5, 4, 3, 0,0]
    print(next_permutation(input_arr))

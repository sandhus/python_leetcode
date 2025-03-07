"""
https://leetcode.com/problems/maximum-subarray/description/
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""

def max_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in nums[1:]:
        current_sum = max(i, current_sum+i)
        max_sum = max(current_sum, max_sum)

    return print(max_sum)


max_sum([8])
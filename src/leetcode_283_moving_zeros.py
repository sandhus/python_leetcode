"""
https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

"""


def move_zeros(arr):
    for i in arr:
        if i == 0:
            id = arr.index(i)
            arr.pop(id)
            arr.append(0)
    return print(arr)


move_zeros([0, 1, 0, 3, 5, 0, 6, 0, 8, 0, 12])
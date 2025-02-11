"""
https://leetcode.com/problems/merge-intervals/description/
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

"""


def merge_intervals(intervals):

    intervals.sort()

    ans = []

    for i, intr in enumerate(intervals):
        if not ans or ans[-1][1] < intr[0]:
            ans.append(intr)
        else:
            ans[-1][1] = max(ans[-1][1], intr[1])

    return print(ans)


merge_intervals([[1,4],[4,5]])
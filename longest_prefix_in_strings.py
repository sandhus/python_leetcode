"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def longest_prefix(strs):
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    return strs[0]

print(longest_prefix(["dog","racecar","car"]))
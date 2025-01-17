"""
Given an array of strings strs, group the
anagrams
together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other

"""


def group_anagrams(strs):

    out = {}

    for st in strs:
        sorted_st = convert_to_sorted_st(st)

        if sorted_st not in out:
            out[sorted_st] = []
        out[sorted_st].append(st)

    return print(list(out.values()))


def convert_to_sorted_st(strr):

    return ''.join(sorted(strr))

group_anagrams(["eat","tea","tan","ate","nat","bat"])

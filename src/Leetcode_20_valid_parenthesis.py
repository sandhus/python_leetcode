"""
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true
"""

def is_valid(s):

    mapping = {")": "(", "]": "[", "}": "{"}
    last_brk = []

    for i in s:
        if i in mapping.values():
            last_brk.append(i)
        elif i in mapping.keys():
            if not last_brk or mapping[i] != last_brk.pop():
                print("invalid")
                return False
    print("valid")
    return True

is_valid("()[()][]{}")

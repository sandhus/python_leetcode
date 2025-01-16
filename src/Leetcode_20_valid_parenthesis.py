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

    valid_paren = [0, 0, 0]
    for i in s:
        print(valid_paren)
        if i == "(":
            valid_paren[0] += 1
        if i == ")":
            valid_paren[0] -= 1
        if i == "{":
            valid_paren[1] += 1
        if i == "}":
            valid_paren[1] -= 1
        if i == "[":
            valid_paren[2] += 1
        if i == "]":
            valid_paren[2] -= 1

    if not (valid_paren[0] >= 0 and valid_paren[1] >= 0 and valid_paren[2] >= 0):
        print("invalid2")
        return False

    if valid_paren != [0, 0, 0]:
        print(valid_paren)
        print("invalid1")
        return False
    print("valid")
    return True

is_valid("()[]{}")

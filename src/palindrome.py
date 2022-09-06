"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


class Palindrome:

    def is_palindrome(self, x):
        n_list = []
        for i in str(x):
            n_list.append(i)
            print(i)
        print(n_list)

        rev_list = n_list.copy()
        rev_list.reverse()

        print(rev_list)

        if rev_list == n_list:
            return True
        else:
            return False

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Ex-
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""


class link_list_sum:

    def addTwoNumbers(self, l1, l2):

        rn = max(len(l1), len(l2))
        if len(l1) != rn:
            for i in range(rn - len(l1)):
                l1.append(0)

        if len(l2) != rn:
            for i in range(rn - len(l2)):
                l2.append(0)

        sum_list = []
        carry1=0
        for i in range (0, rn):
            if not carry1:
                sum1, carry1 = self.sum_with_carry(l1[i], l2[i])
            else:
                sum1, carry1 = self.sum_with_carry(l1[i], l2[i]+carry1)

            sum_list.append(sum1)

        return sum_list


    def sum_with_carry(self, n1, n2):
        sum = n1 + n2
        carry = 0
        if sum >= 10:
            carry = 1
            sum = sum % 10
        return sum, carry

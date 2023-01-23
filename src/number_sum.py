"""
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Eg- Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class num_sum:
    def twoSum(self, nums, target):

        sum = target
        ind = []
        for item in nums:
            num1 = item
            num2 = sum - num1
            ind1 = nums.index(num1)
            try:
                ind2 = nums.index(num2)
            except:
                print("no solution possible in this array")
                break
            print(ind1)
            print(ind2)

            if ind1 != ind2:
                ind.append(ind1)
                ind.append(ind2)

            if ind:
                break

        return ind


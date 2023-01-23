"""
Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.

Consider this array and the target sums.

arr=[3,7,1,2,8,4,5]
target_sum = 20  5+7+8=20
target_sum =21   No Solution
"""


class ThreeNumberSum:

    def ThreeSums(self, array, target):
        sum = target
        solution = []
        for item in array:
            twotarget = sum - item
            for item2 in array:
                if item2 == item:
                    continue
                else:
                    second_nu = twotarget - item2
                    if second_nu == item2 or second_nu == item:
                        continue
                    elif second_nu in array:
                        solution.append(item)
                        solution.append(item2)
                        solution.append(second_nu)

                    elif solution:
                        break
                    else:
                        continue
        if not solution:
            print("no possible solution")
        return solution

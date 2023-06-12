"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith
 balloon. Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so
 she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed
 integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from
 the rope.

Return the minimum time Bob needs to make the rope colorful.

Eample- Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
"""

class Solution:
    def minCost(self, colors, neededTime) -> int:
        count_list = self.find_consecutive_colors(colors)
        min_time=0
        if count_list:

            while len(count_list) > 0:
                min_time = min_time+neededTime[count_list[0]]
                count_list.pop(0)
                count_list.pop(0)
            return min_time
        else:
            print("Rope is already colorful")
            return True



    def find_consecutive_colors(self, in_str):
        count_list=[]
        for i in range(len(in_str)-1):
            if in_str[i] == in_str[i+1]:
                if i in count_list:
                    count_list.append((i + 1))
                else:
                    count_list.append(i)
                    count_list.append((i + 1))

        if count_list:
            return count_list
        else:
            return False


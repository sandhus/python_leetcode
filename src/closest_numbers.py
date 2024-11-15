"""
Given an array of distinct integers, determine the minimum absolute difference between any two elements. Print all element pairs with that difference in ascending order.


Example

numbers = [6,2,4,10]

The minimum absolute difference is 2 and the pairs with that difference are (2,4) and (4,6). When printing element pairs (i,j), they should be ordered ascending first by i and then by j.

2 4
4 6


"""


def closest_numbers(numbers):

    numbers.sort()

    min_diff = numbers[1] - numbers[0]


    for i in range(1, len(numbers)):
        running_diff = numbers[i] - numbers[i-1]
        if running_diff < min_diff:
            min_diff = running_diff

    for i in range(1, len(numbers)):
        running_diff = numbers[i] - numbers[i-1]
        if running_diff == min_diff:
            print(numbers[i-1], numbers[i])


closest_numbers([6,2,4,10])
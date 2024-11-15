"""
Given three sets of distinct coordinates that form a triangle, calculate the area of the triangle. At least one side
of the triangle will be parallel to either the x-axis or the y-axis.

Example

x = [0, 3, 0]

y = [0, 5, 2]

Aligned by index, the 3 coordinates are [0,0], [3,5], [0,2]. The base of the triangle is 2, and the height is 3.
The area of a triangle is (base * height)/2, so 3 * 2 / 2 = 3. All resulting areas will be whole numbers.

"""

def triangle_area(x,y):
    if len(x) != len(y):
        print("Invalid input")
        return False

    # apply heron's formula for X Y co-ordinates

    area = 1/2 * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))

    if area < 0:
        area = area * -1
    return print(area)

triangle_area([0, 1, 0], [0, 0, 2])
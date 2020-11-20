# Write a function that takes in three numbers. These numbers represent the lengths of the sides of a triangle. The function should return the area of a triangle.

from math import sqrt

def area_of_triangle(x, y, z):
    s = 0.5 * (x + y + z)
    s1 = s - x
    s2 = s - y
    s3 = s - z
    s4 = s1 * s2 * s3
    pre_area = s * s4
    area = sqrt(pre_area)
    return area
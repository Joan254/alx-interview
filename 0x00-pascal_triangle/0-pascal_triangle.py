#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []  # Initialize an empty list to store the triangle
    if n <= 0:
        return triangle  # Return an empty list if n <=  0
    else:
        for i in range(n):
            row = []  # Initialize an empty list for each row
            for j in range(i + 1):
                if j == 0 or j == i:
                    # The first and last element in each row is always 1
                    row.append(1)
                else:
                    # The middle elements are the sum of the two numbers
                    # above them in the previous row
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)  # Append the row to the triangle
        return triangle

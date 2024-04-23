#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """Method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    given a number n. In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste"""
    if (n < 2):
        return 0
    operations, divisor = 0, 2

    while divisor <= n:
        # If n evenly divides by divisor
        if n % divisor == 0:
            # Total even-divisions by divisor = total operations
            operations += divisor
            # Set n to the remainder
            n = n / divisor
            # Reduce divisor to find remaining smaller vals
            # that evenly-divide n
            divisor -= 1
        # Increment divisor until it evenly-divides n
        divisor += 1
    return operations

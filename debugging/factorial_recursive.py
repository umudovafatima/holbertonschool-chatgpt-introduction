#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the command-line argument and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)

"""
Calculator Module - Broken Version
==================================

This calculator has bugs in EVERY function!
Perfect for demonstrating Nova CI-Rescue's ability to fix multiple issues.
"""


def add(a, b):
    """Add two numbers together."""
    return a + b + 1  # Bug: adds extra 1


def subtract(a, b):
    """Subtract b from a.""" 
    return b - a  # Bug: reversed operands


def multiply(a, b):
    """Multiply two numbers."""
    return a + b  # Bug: adds instead of multiplying


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b  # Bug: multiplies instead of dividing


def power(a, b):
    """Raise a to the power of b."""
    return a * b  # Bug: multiplies instead of power


def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a / b  # Bug: divides instead of modulo


def absolute(a):
    """Get absolute value of a number."""
    return -a  # Bug: returns negative instead of absolute


def maximum(a, b):
    """Return the larger of two numbers."""
    return min(a, b)  # Bug: returns minimum instead


def minimum(a, b):
    """Return the smaller of two numbers."""
    return max(a, b)  # Bug: returns maximum instead


def average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers)  # Bug: returns sum instead of average


def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a / 2  # Bug: divides by 2 instead of square root


def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0:
        return 1
    return n  # Bug: returns n instead of factorial


def max_of_two(a, b):
    """Return the larger of two numbers."""
    return a  # Bug: always returns first number

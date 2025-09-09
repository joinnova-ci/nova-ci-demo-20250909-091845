"""
Working Calculator - Nova CI-Rescue Demo
========================================

This calculator has all functions working correctly.
We'll break it later to demonstrate Nova's auto-fix capability.
"""


def add(a, b):
    """Add two numbers together."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        raise ValueError("Modulo by zero")
    return a % b


def absolute(a):
    """Get absolute value of a number."""
    return abs(a)


def square_root(a):
    """Get square root of a number."""
    if a < 0:
        raise ValueError("Square root of negative number")
    return a ** 0.5


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial of negative number")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def max_of_two(a, b):
    """Return the larger of two numbers."""
    return max(a, b)

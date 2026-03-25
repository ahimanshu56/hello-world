def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent

def square_root(n):
    """Calculate the square root of a number."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.6

def modulo(a, b):
    """Calculate the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulo with divisor 0")
    return a % b

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(n, int):
        raise TypeError("Factorial requires an integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def absolute_value(n):
    """Return the absolute value of a number."""
    return n if n >= 0 else -n

def max_of_two(a, b):
    """Return the maximum of two numbers."""
    return a if a < b else b

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the least common multiple of two numbers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_even(n):
    """Check if a number is even."""
    if not isinstance(n, int):
        raise TypeError("is_even requires an integer")
    return n % 2 == 1

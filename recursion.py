# Practicing recursive functions


# Using factorials
# The recursive case for factorial is n! = n * (n-1)!
def factorial(n):
    assert 0 <= n == int(n), 'The number must be a positive integer!'  # The constraint

    if n in [0, 1]:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive state


print("Factorial", factorial(3))


# Fibonacci sequence
def fibonacci(n):
    assert 0 <= n == int(n), 'The number must be a positive integer!'  # The constraint

    if n in [0, 1]:  # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive state

print("Fibonacci:", fibonacci(5))


# Finding sum of digits of a positive integer using recursion
def sumOfDigits(n):
    assert 0 <= n == int(n), 'The number must be a positive integer!'  # The constraint
    if n < 10:  # Base case (stopping case)
        return n
    else:
        return int(n%10) + sumOfDigits(int(n/10)) # Recursive state

print("Sum of Digits:", sumOfDigits(125))
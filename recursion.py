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


# Calculating power of a number using recursion
def powerOfNumber(base, exp):
    assert 0 <= base == int(base), 'The base number must be a positive integer!'
    assert 0 <= exp == int(exp), 'The exponent must be a positive integer!'  # The constraint

    if exp == 0:  # Stopping Case
        return 1
    elif exp == 1:  # Stopping Case
        return base
    else:
        return base * powerOfNumber(base, exp - 1)

print("Power of a number:", powerOfNumber(3, 3))


# Finding greatest common divisor
def gcd(x, y):
    assert 0 <= x == int(x) and x > y, 'X must be a positive integer and greater than y!'  # The constraint
    assert 0 <= y == int(y), 'Y must be a positive integer!'  # The constraint

    if x % y != 0:
        return gcd(y, x%y)  # Flow
    else:
        return y  # Base case

print("GCD:", gcd(456, 324))


# Convert number from decimal to binary using recursion
def decToBinary(n):
    assert 0 <= n == int(n), 'n must be a positive integer!'  # The constraint
    if n // 2 == 0:
        return str(n % 2)  # Stop case
    else:
        return decToBinary(n // 2) + str(n % 2)  # Flow

print("Decimal to Binary:", decToBinary(27))
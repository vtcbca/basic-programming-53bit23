
import math

def factorial_using_math_module(n):
    return math.factorial(n)

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_using_math_module(number)}")

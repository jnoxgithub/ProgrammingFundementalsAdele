#Write a program that uses the `math` module to 
#calculate the square root and factorial of a number.
#Google had to help me with this one due to me having no concept of what a factorial number is.
import math

def calculate_sqrt_and_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."

    # Calculate the square root
    sqrt_result = math.sqrt(number)
    
    # Calculate the factorial
    factorial_result = math.factorial(number)
    
    return sqrt_result, factorial_result

# Example usage:
number = 69
sqrt_result, factorial_result = calculate_sqrt_and_factorial(number)

print(f"Square root of {number}: {sqrt_result}")
print(f"Factorial of {number}: {factorial_result}")
#Write a program that checks if a number is positive, negative, or zero.

#User input
number = float(input("Enter a number: "))

#Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
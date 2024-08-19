#Write a function that takes a list of numbers and returns the list sorted in ascending order.
#The task was slightly unclear, so I just listed some random numbers (see in numbers=)

def sort_list(numbers):
    #Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    return sorted_numbers

#List of numbers
numbers = [1, 17, 48, 231, 3123, 9123]

#Get the sorted list
sorted_numbers = sort_list(numbers)

#Print the sorted list
print("Sorted list:", sorted_numbers)

#Should output something to the effect of Sorted list: [1, 17, 48, 231, 3123, 9123]
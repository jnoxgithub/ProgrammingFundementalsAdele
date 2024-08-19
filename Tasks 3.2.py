#Write a function that counts the frequency of each character in a string.
#Again the tasks is a little open ended so I just took "she sells seashells by the seashore"
#Then counted the frequency the letter s was used.

def count_char_frequency(s, char_to_count):
    # Create an empty dictionary to store character frequencies
    frequency = {}
    
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, add the character to the dictionary with count 1
        else:
            frequency[char] = 1
    
    # Return the count for the specific character if it exists
    return frequency.get(char_to_count, 0)

# Given string
text = "she sells seashells by the seashore"

# Count the frequency of 'S'
s_count = count_char_frequency(text, 's')
print("Frequency of 's':", s_count)
#Write a function that checks if a given string is a palindrome.

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_s = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
string = "racecar"
print(f"Is the string '{string}' a palindrome?", is_palindrome(string))
#Again I had to google what a palindrome was
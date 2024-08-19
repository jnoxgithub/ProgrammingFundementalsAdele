#Write a function that reads a text file and prints its contents.
def read_and_print_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            content = file.read()
            # Print the contents
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")

file_path = 'C:\\Users\\jorda\\Documents\\Tasks 5.1.txt'

# Call the function
read_and_print_file(file_path)
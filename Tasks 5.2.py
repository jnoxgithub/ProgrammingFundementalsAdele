def write_to_file(file_path, content):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the content to the file
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except IOError:
        print(f"Error writing to file: {file_path}")

# Example usage
file_path = 'C:\\Users\\jorda\\Documents\\Tasks 5.1.txt'
content = 'no problem CPL'

# Call the function
write_to_file(file_path, content)
# Function to print the first 10 numbers of the Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

# Main part of the script
if __name__ == "__main__":
    # Number of Fibonacci numbers to print
    num_terms = 10
    print(f"The first {num_terms} numbers of the Fibonacci series are:")
    fibonacci_series(num_terms)

    #I had to google what the fibonacci sequence was rip
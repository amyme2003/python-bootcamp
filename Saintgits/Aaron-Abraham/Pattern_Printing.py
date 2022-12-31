# Function to print the pattern
def print_pattern():
    
    for i in range(1, 6):
        for j in range(i):
        # Print the number i
            print(i, end=" ")
        # Move to the next line after printing the row
        print()

# Call the function to print the pattern
print_pattern()

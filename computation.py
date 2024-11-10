def add_numbers(a, b):
    """
    Add two numbers and return the result
    """
    return a + b

def print_numbers(a, b):
    """
    Print two numbers in a formatted way
    """
    print(f"First number: {a}")
    print(f"Second number: {b}")

def main():
    # Example usage of our functions
    num1 = 10
    num2 = 20
    
    # Print the numbers
    print("Demonstrating print_numbers function:")
    print_numbers(num1, num2)
    
    # Add the numbers and show result
    print("\nDemonstrating add_numbers function:")
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

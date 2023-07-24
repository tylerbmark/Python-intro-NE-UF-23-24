def binary_to_list(binary_string):
    # Remove non-binary characters
    binary_string = ''.join(char for char in binary_string if char in '01')

    # Remove any leading zeros
    binary_string = binary_string.lstrip('0')

    # Convert binary string to a list of integers
    binary_list = [int(bit) for bit in binary_string]

    return binary_list

# Example usage
binary_string = input("Enter a binary string: ")
binary_list = binary_to_list(binary_string)
print("Binary List:", binary_list)
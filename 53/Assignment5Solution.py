def is_palindrome_reversed(input_string):
    return input_string == ''.join(reversed(input_string))

# Example usage
input_string = "madam"
print(is_palindrome_reversed(input_string))  # Output: True

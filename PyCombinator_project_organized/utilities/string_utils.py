
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

# Example Usage
input_string = "madam"
print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")

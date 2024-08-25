#This defines a class called Stack, which will contain the methods and attributes that define a stack.
class Stack:
    def __init__(self):
        self.items = []
#Pushing an element to the stack and appending it to the instance of the class
    def push(self, item):
        self.items.append(item)
#checks if the stack is empty and removes and returns the last element if it's not,if it's not it returns none
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(string):
    stack = Stack()
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(string.lower().split())

    # Push all characters of the string onto the stack
    for char in cleaned_string:
        stack.push(char)

    # Rebuild the string by popping from the stack
    reversed_string = ''.join([stack.pop() for _ in range(len(cleaned_string))])

    return cleaned_string == reversed_string

# Test the function
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))  # Output: False

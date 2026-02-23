 # Question 17: Palindrome Checker 

value = input("Enter word/number: ")

print("Original:", value)

# Reverse the value
reversed_value = value[::-1]

print("Reversed:", reversed_value)

# Ignore case (for words)
if value.lower() == reversed_value.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")
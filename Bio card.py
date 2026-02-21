
# Question 1: Personal Bio Card

# Storing the detail of the student
name = "Chethana V"
age = 20
course = "Python Programming"
college = "East Point College"
email = "chethanavenkatesh02@gmail.com"

# Creating the format lines
line1 = f"Name    : {name}"
line2 = f"Age     : {age} years"
line3 = f"Course  : {course}"
line4 = f"College : {college}"
line5 = f"Email   : {email}"

# Store all lines in a list
details = [line1, line2, line3, line4, line5]

# Calculate the width for the program 
max_length = max(len(line) for line in details)
box_width = max_length + 4  # extra padding

# Adding the width 
top_border = "╔" + "═" * box_width + "╗"
middle_border = "╠" + "═" * box_width + "╣"
bottom_border = "╚" + "═" * box_width + "╝"

# Print formatted card
print(top_border)
print("║" + "STUDENT BIO CARD".center(box_width) + "║")
print(middle_border)

for line in details:
    print("║  " + line.ljust(max_length) + "  ║")

print(bottom_border)
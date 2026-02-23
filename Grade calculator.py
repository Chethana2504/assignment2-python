# Question 6 - Grade Calculator

# Input marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Store marks in a list
marks = [sub1, sub2, sub3, sub4, sub5]

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Determine pass/fail
if all(mark >= 40 for mark in marks):
    result = "Pass"
else:
    result = "Fail"

# Display results
print("\nMarks in each subject:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
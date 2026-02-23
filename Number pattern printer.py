# Question 11 - number pattern printer

print("Choose a pattern (1-4):")
print("1. Increasing numbers")
print("2. Repeating numbers")
print("3. Decreasing triangle")
print("4. Palindromic pyramid")

pattern = int(input("Enter pattern number: "))
height = int(input("Enter the height of the pattern: "))

if pattern == 1:
    for i in range(1, height+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

elif pattern == 2:
    for i in range(1, height+1):
        for j in range(i):
            print(i, end=" ")
        print()

elif pattern == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif pattern == 4:
    for i in range(1, height+1):
        for j in range(1, i+1):
            print(j, end="")
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid pattern number!")
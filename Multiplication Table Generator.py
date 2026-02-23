#   Question 12 - number multiplication table

num = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {num}")
for i in range(1, end+1):
    print(f"{num} x {i} = {num*i}")

# table 1-10
print("\nFull Multiplication Table (1-10):")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")  
    print()
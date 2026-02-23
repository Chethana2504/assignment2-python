# Question 13 - sum and average

count = int(input("How many numbers you want to add :"))

numbers = []

for i in range(count):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / count

print("Sum:", total)
print("Average:", average)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
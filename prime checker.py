# Question 15 - Prime Number Checker 

# Check if a single number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Part 2: Prime numbers in range

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:")

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
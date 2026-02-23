#Question 14 - Factorial Calculator

#enter the number
num = int(input("Enter a number: "))

# Handle 0 and negative numbers
if num < 0:
    print("Factorial not possible for negative numbers")

elif num == 0:
    print("0! = 1")

else:
    fact = 1
    i = num

    print(num, "! =", end=" ")

    while i >= 1:
        print(i, end=" ")
        fact = fact * i
        i = i - 1

    print("=", fact)
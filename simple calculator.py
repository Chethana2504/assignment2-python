# Question 2: Simple Calculator

# Taking the input 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:")

# Addition
print(a, "+", b, "=", a + b)

# Subtraction
print(a, "-", b, "=", a - b)

# Multiplication
print(a, "*", b, "=", a * b)

# Division
if b != 0:
    print(a, "/", b, "=", round(a / b))
else:
    print("Division not possible")

# Modulus
if b != 0:
    print(a, "%", b, "=", a % b)
else:
    print("Modulus not possible")

# Exponentiation
print(a, "^", b, "=", a ** b)
 # Question 18 - Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


def calculator():

    print("1.Add  2.Subtract  3.Multiply")
    print("4.Divide  5.Modulus  6.Power  7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        print("Exit")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))

    elif choice == 2:
        print("Result:", subtract(a, b))

    elif choice == 3:
        print("Result:", multiply(a, b))

    elif choice == 4:
        print("Result:", divide(a, b))

    elif choice == 5:
        print("Result:", modulus(a, b))

    elif choice == 6:
        print("Result:", power(a, b))


calculator()
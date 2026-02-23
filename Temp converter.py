# Question 7 - Temperature Converter

while True:
    print("\nTemperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    elif choice == '3':
        c = float(input("Enter Celsius: "))
        k = c + 273.15
        print(f"{c}°C = {k:.2f}K")
    elif choice == '4':
        k = float(input("Enter Kelvin: "))
        c = k - 273.15
        print(f"{k}K = {c:.2f}°C")
    elif choice == '5':
        f = float(input("Enter Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f}°F = {k:.2f}K")
    elif choice == '6':
        k = float(input("Enter Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"{k}K = {f:.2f}°F")
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
#  Question 8 - Leap Year Checker

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a Leap Year")
    if year % 400 == 0:
        print("Reason: Divisible by 400")
    elif year % 100 == 0:
        print("Reason: Divisible by 100 but not 400 → Not a leap year normally, but exception handled")
    else:
        print("Reason: Divisible by 4 but not by 100")
else:
    print(f"{year} is NOT a Leap Year")
    if year % 4 != 0:
        print("Reason: Not divisible by 4")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but not by 400")
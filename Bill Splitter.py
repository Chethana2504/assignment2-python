# Question 5: Bill Splitter

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculations
tax_amount = total_bill * tax_percent / 100
bill_after_tax = total_bill + tax_amount

tip_amount = bill_after_tax * tip_percent / 100
final_total = bill_after_tax + tip_amount

if people > 0:
    per_person = final_total / people
else:
    per_person = 0

print("\n=== BILL BREAKDOWN ===")
print("Subtotal:", total_bill)
print("Tax Amount:", round(tax_amount, 2))
print("After Tax:", round(bill_after_tax, 2))
print("Tip Amount:", round(tip_amount, 2))
print("Total Bill:", round(final_total, 2))
print("Amount Per Person:", round(per_person, 2))
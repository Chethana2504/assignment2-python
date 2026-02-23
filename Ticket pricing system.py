# Question 9 - Ticket Pricing System

# Inputs
age = int(input("Enter your age: "))
day = input("Enter day of the week: ").strip().lower()
num_tickets = int(input("Enter number of tickets: "))

# Age based pricing
if age < 3:
    base_price = 0
elif 3 <= age <= 12:
    base_price = 150
elif 13 <= age <= 59:
    base_price = 300
else:  # 60+
    base_price = 200

# Discount
if day in ["monday", "tuesday", "wednesday", "thursday"]:
    discount = 0
elif day in ["friday", "saturday", "sunday"]:
    discount = 0.2 * base_price

price_after_discount = base_price - discount
total_amount = price_after_discount * num_tickets

# Display results
print("\n===== Ticket Summary =====")
print(f"Base Price: ₹{base_price}")
print(f"Discount: ₹{discount:.2f}")
print(f"Price after Discount: ₹{price_after_discount:.2f}")
print(f"Number of Tickets: {num_tickets}")
print(f"Total Amount: ₹{total_amount:.2f}")
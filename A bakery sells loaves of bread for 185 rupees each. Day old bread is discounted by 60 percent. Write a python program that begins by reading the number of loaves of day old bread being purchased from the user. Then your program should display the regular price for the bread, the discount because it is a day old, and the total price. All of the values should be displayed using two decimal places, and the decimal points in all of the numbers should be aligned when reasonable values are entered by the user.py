# Read the number of loaves of day-old bread from the user
loaves = int(input("Enter the number of loaves of day-old bread: "))

# Regular price of each loaf
regular_price = 185

# Discount for day-old bread
discount = 0.60

# Calculate total price
total_regular_price = loaves * regular_price
total_discount = total_regular_price * discount
total_price = total_regular_price - total_discount

# Display the prices with two decimal places
print(f"Regular Price: {total_regular_price:.2f} rupees")
print(f"Discount: {total_discount:.2f} rupees")
print(f"Total Price: {total_price:.2f} rupees")

def calculate_shipping_charge(num_items):
    if num_items == 1:
        return 750.00
    else:
        return 750.00 + (num_items - 1) * 200.00

# Read the number of items purchased from the user
num_items = int(input("Enter the number of items purchased: "))

# Calculate and display the shipping charge
shipping_charge = calculate_shipping_charge(num_items)
print(f"Shipping charge for {num_items} items: ${shipping_charge:.2f}")

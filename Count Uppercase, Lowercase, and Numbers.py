upper_count = 0
lower_count = 0
number_count = 0

while True:
    char = input("Enter a character: ")
    
    if char == '*':
        break
    
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        number_count += 1

print("Uppercase count:", upper_count)
print("Lowercase count:", lower_count)
print("Number count:", number_count)

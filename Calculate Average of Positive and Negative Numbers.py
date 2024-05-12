positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
    
    if num >= 0:
        positive_sum += num
        positive_count += 1
    else:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    average_positive = positive_sum / positive_count
    print(f"Average of positive numbers: {average_positive}")
else:
    print("No positive numbers entered.")

if negative_count > 0:
    average_negative = negative_sum / negative_count
    print(f"Average of negative numbers: {average_negative}")
else:
    print("No negative numbers entered.")

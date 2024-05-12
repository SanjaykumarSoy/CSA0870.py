start_num = float(input("Enter the starting number: "))
max_lines = int(input("Max number of lines to be printed: "))

current_num = start_num
for i in range(max_lines):
    for j in range(i+1):
        print("{:.1f}".format(current_num), end=" ")
        current_num += 0.1
    print()

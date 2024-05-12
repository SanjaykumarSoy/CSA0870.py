list_of_elements = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

sorted_list = sorted(list_of_elements)
mth_max = sorted_list[-M]
nth_min = sorted_list[N-1]
sum_result = mth_max + nth_min
diff_result = abs(mth_max - nth_min)

print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {diff_result}")

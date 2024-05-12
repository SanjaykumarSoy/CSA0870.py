from math import comb

def generate_binomial_coefficients_triangle(n):
    triangle = [[comb(i, j) for j in range(i + 1)] for i in range(n)]
    return triangle

def sum_of_nth_row_binomial_coefficients(n):
    row = [comb(n, i) for i in range(n + 1)]
    return sum(row)

n = 5
triangle = generate_binomial_coefficients_triangle(n)
sum_of_nth_row = sum_of_nth_row_binomial_coefficients(n)

print(triangle)
print(f"Sum of elements in the {n}th row: {sum_of_nth_row}")

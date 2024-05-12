def is_perfect_number(num):
    sum_factors = sum([i for i in range(1, num) if num % i == 0])
    return sum_factors == num

def factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def print_perfect_numbers_factors(n, m):
    count = 0
    num = 1

    while count < n:
        if is_perfect_number(num):
            factors_list = factors(num)[:m]
            print(f"Perfect Number {count+1}: {num}, Factors: {factors_list}")
            count += 1
        num += 1

n = 5  # Number of perfect numbers to print
m = 3  # Number of factors to display for each perfect number
print_perfect_numbers_factors(n, m)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def count_factors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

n = 6
fact = factorial(n)
factors = count_factors(n)

print(f"{n} Factorial: {fact}")
print(f"Number of factors for {n}: {factors}")

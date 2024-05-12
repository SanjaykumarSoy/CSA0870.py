def numSquares(n):
    dp = [0] + [float('inf')] * n
    for i in range(1, n + 1):
        dp[i] = min(dp[i - j*j] + 1 for j in range(1, int(i**0.5) + 1))
    return dp[n]

# Example Usage
n = 12
print(numSquares(n))  # Output: 3

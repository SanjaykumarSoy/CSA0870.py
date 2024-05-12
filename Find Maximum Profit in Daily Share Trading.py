def max_profit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    max_profit = 0
    
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit

# Example Usage
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output: 7

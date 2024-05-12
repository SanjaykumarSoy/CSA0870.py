def matches(s1, s2):
    return sum(1 for x, y in zip(s1, s2) if x == y)

# Test the function
s1 = "what"
s2 = "watch"
print(matches(s1, s2))  # Output: 1

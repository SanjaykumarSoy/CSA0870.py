def is_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# Test the function
s1 = "egg"
t1 = "add"
print(is_isomorphic(s1, t1))  # Output: True

s2 = "foo"
t2 = "bar"
print(is_isomorphic(s2, t2))  # Output: False

from itertools import product

def letter_combinations(digits):
    if not digits:
        return []
    
    phone_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    return [''.join(comb) for comb in product(*(phone_letters[d] for d in digits))]

# Test the function with the provided input
digits = "23"
output = letter_combinations(digits)
print(output)

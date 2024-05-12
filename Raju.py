def is_mirror_number(number):
    return str(number) == str(number)[::-1]
number = 12321
print(is_mirror_number(number))

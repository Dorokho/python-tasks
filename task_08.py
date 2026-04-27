def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    
    result = 1
    found_digit = False

    for ch in str(inputs):
        if ch.isdigit():
            result *= int(ch)
            found_digit = True

    return result if found_digit else None

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
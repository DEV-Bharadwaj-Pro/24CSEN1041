def decimal_to_base(num, base, precision=10):
    value_to_symbol = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D',
        14: 'E', 15: 'F'
    }

    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert integer part
    if integer_part == 0:
        int_result = "0"
    else:
        int_result = ""
        while integer_part > 0:
            remainder = integer_part % base
            int_result = value_to_symbol[remainder] + int_result
            integer_part //= base

    # Convert fractional part
    frac_result = ""
    count = 0
    while fractional_part > 0 and count < precision:
        fractional_part *= base
        digit = int(fractional_part)
        frac_result += value_to_symbol[digit]
        fractional_part -= digit
        count += 1

    if frac_result:
        return int_result + "." + frac_result
    else:
        return int_result


def base_to_decimal(num_str, base):
    symbol_to_value = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13,
        'E': 14, 'F': 15
    }

    num_str = num_str.upper()

    if '.' in num_str:
        int_part, frac_part = num_str.split('.')
    else:
        int_part, frac_part = num_str, ""

    decimal_value = 0

    # Integer part
    power = len(int_part) - 1
    for digit in int_part:
        decimal_value += symbol_to_value[digit] * (base ** power)
        power -= 1

    # Fractional part
    power = -1
    for digit in frac_part:
        decimal_value += symbol_to_value[digit] * (base ** power)
        power -= 1

    return decimal_value


# ---------- USER INPUT ----------
number = input("Enter the number: ")
input_base = int(input("Enter input base (2–16): "))
output_base = int(input("Enter output base (2–16): "))

if not (2 <= input_base <= 16 and 2 <= output_base <= 16):
    print("Base must be between 2 and 16")
else:
    decimal_number = base_to_decimal(number, input_base)
    result = decimal_to_base(decimal_number, output_base)
    print("Result:", result)

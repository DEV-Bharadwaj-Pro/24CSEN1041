def decimal_to_base(num, base):
    value_to_symbol = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D',
        14: 'E', 15: 'F', 16: 'G'
    }

    result = ""

    while num > 0:
        remainder = num % base
        result = value_to_symbol[remainder] + result
        num //= base

    return result


number = int(input("Enter a decimal number: "))
base = int(input("Enter base: "))

if number == 0:
    print("Result: 0")
else:
    print("Result:", decimal_to_base(number, base))

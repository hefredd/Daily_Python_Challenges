def hex_to_decimal(hex):
    decimal = 0
    power = 0
    hex_table = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    for digit in reversed(hex):
        upper_digit = digit.upper()
        if upper_digit.isdigit():
            integer = int(upper_digit)
        else:
            # integer = (ord(upper_digit) - ord("A")) + 10
            integer = hex_table[upper_digit]
        converted_no = integer * (16 ** power)
        decimal += converted_no
        power += 1
    return decimal
    # return int(hex, 16)
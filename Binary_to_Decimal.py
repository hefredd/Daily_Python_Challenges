def to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        integer = int(digit)
        converted_int = integer * (2 ** power)
        decimal += converted_int
        power += 1
    #return int(binary, 2)
    return decimal 
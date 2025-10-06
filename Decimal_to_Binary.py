def to_binary(decimal):
    if decimal == 0:
        return 0
    binary_string = ""
    current_no = decimal
    while current_no > 0:
        remainder = current_no % 2
        binary_string = str(remainder) + binary_string
        current_no = current_no // 2

    # using the bin() to convert
    # binary = bin(decimal)
    # return binary[2:]

    return binary_string
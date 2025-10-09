def to_luminosity(char):
    if "0" <= char <= "9":
        return int(char)
    elif "A" <= char <= "Z":
        return ord(char) - ord("A") + 10
    else:
        raise ValueError(f"Invalid luminosity character: {char}") 
def has_exoplanet(readings):
    if not readings:
        return False
    numerical_list = [to_luminosity(char) for char in readings]
    total_sum = sum(numerical_list)
    count = len(numerical_list)
    average = total_sum / count
    exoplanet_threshold = average * 0.8

    for reading in numerical_list:
        if reading <= exoplanet_threshold:
            return True
    return False 
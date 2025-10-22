def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    if current_f < target_f:
        to_heat = round(target_f - current_f, 1)
        return f"Heat: {to_heat} degrees Fahrenheit"
    elif current_f > target_f:
        to_cool = round(current_f - target_f, 1)
        return f"Cool: {to_cool} degrees Fahrenheit"
    else:
        return "Hold"
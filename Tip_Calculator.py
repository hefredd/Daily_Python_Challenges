def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.replace('$', ''))
    custom = float(custom_tip.replace('%', '')) / 100
    tip_list = [0.15, 0.20] + [custom]
    tip_values = []
    for tip in tip_list:
        meal = price * tip
        rounded_tip = round(meal, 2)
        formated_tip = f"${rounded_tip:.2f}"
        tip_values.append(formated_tip)

    return tip_values
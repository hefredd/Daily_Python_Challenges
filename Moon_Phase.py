from datetime import date
def moon_phase(date_string):
    reference_date = date(2000, 1, 6)
    input_date = date.fromisoformat(date_string)
    date_difference = input_date - reference_date
    days = date_difference.days + 1
    cycle_days = days % 28
    if cycle_days == 0:
        cycle_days = 28
    if cycle_days >= 22:
        return "Waning"
    elif cycle_days >= 15:
        return "Full"
    elif cycle_days >= 8:
        return "Waxing"
    else:
        return "New"
def to_12(time):
    hour_part = int(time[:2])
    min_part = time[2:]
    if hour_part < 12:
        meridiem = "AM"
    else:
        meridiem = "PM"
    if hour_part == 0:
        twelve_hr = 12
    # elif hour_part == 12:
        # twelve_hr = 12
    elif hour_part > 12:
        twelve_hr = hour_part - 12
    else:
        twelve_hr = hour_part
   
    return f"{twelve_hr}:{min_part} {meridiem}"
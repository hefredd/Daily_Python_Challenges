def send_message(route):
    speed = 300000
    transmission_delay = 0.5
    total_distance = sum(route)
    time_taken = total_distance / speed
    no_of_satellites = len(route) - 1
    total_delay = no_of_satellites * transmission_delay
    total_time_taken = time_taken + total_delay
    rounded_time = round(total_time_taken, 4)

    return rounded_time
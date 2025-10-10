def launch_fuel(payload):
    current_fuel = 0
    needed_fuel = payload / 5
    while needed_fuel >= 1:
        current_fuel += needed_fuel
        needed_fuel = needed_fuel / 5
    current_fuel += needed_fuel

    return round(current_fuel, 1)
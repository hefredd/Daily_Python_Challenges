def goldilocks_zone(mass):
    luminosity = mass **  3.5
    squareroot_luminosity = luminosity ** 0.5
    start = 0.95 * squareroot_luminosity
    end = 1.37 * squareroot_luminosity
    start_rounded = round(start, 2)
    end_rounded = round(end, 2)
    distance = [start_rounded, end_rounded]

    return distance
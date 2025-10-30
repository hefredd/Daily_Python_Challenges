def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def nth_prime(n):
    if n <= 0:
        return ValueError("Input 'n' must be a positive integer.")
    counter = 0
    number = 2
    while counter < n:
        if is_prime(number):
            counter += 1
            if counter == n:
                return number
        number += 1   
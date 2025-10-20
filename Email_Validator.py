import re
def validate(email):
    pattern = r"^([a-zA-Z0-9-_]+(\.[a-zA-Z0-9-_]+)*)(?<!\.)@([a-zA-Z0-9!_-]+(\.[a-zA-Z0-9_!-]+)*)\.([a-zA-Z]{2,})$"
    return re.match(pattern, email) is not None
def check_strength(password):
    rule_count = 0
    if len(password) >= 8:
        rule_count += 1
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_upper and has_lower:
        rule_count += 1
    if any(char.isdigit() for char in password):
        rule_count += 1
    special_characters = "!@#$%^&*"
    if any(char in special_characters for char in password):
        rule_count += 1
    if rule_count < 2:
        return "weak"
    elif rule_count < 4:
        return "medium"
    else:
        return "strong"
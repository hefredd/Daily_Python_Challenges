# import re
def mask(card):
    if '-' in card:
        separator = '-'
    else:
        separator = ' '
    sets = card.split(separator)
    masked_card = []
    for i, set in enumerate(sets):
        if i < 3:
            masked_card.append('****')
        else:
            masked_card.append(set)
    return separator.join(masked_card)
    # replace any digit that has at least 4 digits following it with '*'
    # return re.sub(r'\d(?=(?:.*\d){4})', '*', card)
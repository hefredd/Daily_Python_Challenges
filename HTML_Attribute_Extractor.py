import re
def extract_attributes(element):
    pattern = r'(\w+)\s*=\s*"([^"]*)"'
    attributes = re.findall(pattern, element)
    formated_attributes = []
    for attr, value in attributes:
        prop = f"{attr}, {value}"
        formated_attributes.append(prop)
        
    return formated_attributes 
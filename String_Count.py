import re
def count(text, parameter):
    # if not parameter:
        # return len(text) + 1
    return len(re.findall(f"(?={re.escape(parameter)})", text))

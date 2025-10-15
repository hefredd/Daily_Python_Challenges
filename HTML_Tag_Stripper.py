import re
def strip_tags(html):
    plain_text = re.sub("<.*?>", "", html)
    return plain_text
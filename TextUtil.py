def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Function to convert
def listToString(s):
    str1 = " "
    return str1.join(s)


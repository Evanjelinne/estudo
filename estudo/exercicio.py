def on(text):
    return [word for word in text.split() if word[-2:] == 'on']

def z(text):
    return [word for word in text.split() if 'z' in word]

def ne(text):
    return [word for word in text.split() if 'ne' in word]

def Mai_min(text):
    return [word for word in text.split() if word[1:] == word.lower()[1:]]
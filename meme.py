import random


def ran_cap(text_input):
    chars = list(text_input)
    for i in range(len(chars)):
        rand = random.randrange(2)
        if rand == 0:
            chars[i] = chars[i].upper()
        else:
            chars[i] = chars[i].lower()
    output = ""
    return output.join(chars)

def vaporwave(text_input):
    chars = list(text_input)
    for i in range(len(chars)):
        chars[i] = chars[i].upper()
    output = " "
    return output.join(chars)

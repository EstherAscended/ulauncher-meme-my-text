import random
import re


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


def reverse(text_input):
    chars = list(text_input)
    chars.reverse()
    output = ""
    return output.join(chars)

def pig_latin(text_input):
    words = text_input.split()
    chars = []
    output_list = []
    for word in words:
        chars.append(list(word))

    consonants = re.compile(r"[bcdfghjklmnpqrstvwxyz]", re.IGNORECASE)
    vowels = re.compile(r"[aeiou]", re.IGNORECASE)

    for i in range(len(chars)):
        add_ay = False
        pigged_word = chars[i][0:]

        for n in range(2):
            if vowels.match(pigged_word[0]) and n == 0:
                end = ["w", "a", "y"]
                pigged_word.append(pigged_word.pop(0))
                pigged_word += end
                break
            if consonants.match(pigged_word[0]):
                pigged_word.append(pigged_word.pop(0))
                add_ay = True

        if add_ay:
            end = ["a", "y"]
            pigged_word += end

        word_output = ""
        output_list.append(word_output.join(pigged_word))

    output = " "
    return output.join(output_list)

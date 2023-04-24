
def is_space(let):
    return let == ' ' or let == '\n' or let == '\t'

def reverts_words(text):
    i = 0
    while i < len(text):
        while is_space(text[i]):
            i += 1
        j = i
        while j < len(text) and not is_space(text[j]):
            j += 1
        tmp = j
        j -= 1
        while j > i:
            text[i], text[j] = text[j], text[i]
            i += 1
            j -= 1

        i = tmp

text = list("\tHello my friend!\nI glad to see you!")

print("".join(text))

reverts_words(text)

print("".join(text))

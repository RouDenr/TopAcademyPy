
def print_pref(text):
    s_text = text.split(" ")
    for i in range(len(s_text[0])):
        is_pref = True
        for j in s_text:
            if i >= len(j) or j[i] != s_text[0][i]:
                is_pref = False
                break
        if is_pref:
            print(s_text[0][i], end="")
        else:
            break
    print()


def print_max(text):
    s_text = text.split(" ")
    for i in range(len(s_text[0]) - 1):
        for k in range(i, len(s_text[0])):
            is_pref = True
            for j in s_text:
                if k >= len(j) or j[k] != s_text[0][k]:
                    is_pref = False
                    break
            if is_pref:
                print(s_text[0][k], end="")
            else:
                break
    print()

text = "foooooooo foou foo"

print_pref(text)

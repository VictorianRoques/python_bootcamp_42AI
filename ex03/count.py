import string

def text_analyser(text = ""):
    total = 0
    upper = 0
    lower = 0
    ponctuation = 0
    space = 0
    if (text == ""):
        text = input("Enter a text please:\n")
    for x in text:
        total = total + 1
        if x.isupper() == 1:
            upper = upper + 1
        elif x.islower() == 1:
            lower = lower + 1
        elif x in string.punctuation:
            ponctuation = ponctuation + 1
        elif x.isspace() == 1:
            space = space + 1
    print(f"The text contains {total} characters:")
    print(f"- {upper} upper letters")
    print(f"- {lower} lower letters")
    print(f"- {ponctuation} marks")
    print(f"- {space} spaces")
    return

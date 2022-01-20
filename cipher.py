def solve(text):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        if(i%2==0):
            s=13
        else:
            s=5

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text = input()
print(solve(text))
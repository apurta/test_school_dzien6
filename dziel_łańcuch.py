numbers = "123,21,45,68"

# efekt: print(split(numbers, ",")) == ["123","21","45","68"]
# efekt: print(split(numbers, "2")) == ["1", "3,", "1,45,68"]


def split(text, sep):

    parts = []
    current_part = ""

    for char in text:
        if char != sep:
            current_part += char
        else:
            parts.append(current_part)
            current_part = ""
    parts.append(current_part)
    return parts


print(split(numbers, "2"))

print()


###### join
print(",".join(["a", "b", "c"]))


def split2(text, sep):

    parts = []
    current_part = []

    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append("".join(current_part))
            current_part = []
    parts.append("".join(current_part))
    return parts

print(split2(numbers, "2"))

###### jeszcze innny sposób
print()
def split3(text, sep):
    parts = []
    start = 0

    for current, char in enumerate(text):
        if char == sep:
            parts.append(text[start:current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split3(numbers, "2"))
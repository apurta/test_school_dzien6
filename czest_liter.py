
slowo = "kotek34567"
dict = {}

# import string
# print(string.ascii_lowercase)

#########
for letter in slowo:
    if letter not in string.ascii_lowercase:
        dict[other] =+ 1
    else letter in string.ascii_lowercase:
        dict[letter] = + 1


#rozwiazanie

text = "Ala ma kota!"
# tak ma być : dict = {'a': 4, "l":1, "m":1, "k":1, "o":1, "t":1, "others":3}
hist = {}

def histogram(text):

    hist = {}

    for char in text.lower():
        if char.isalpha():
            hist[char] = hist.get(char, 0) +1
        else:
            hist["others"] = hist.get("others", 0) + 1
    return hist

print(histogram("Ala MA KOTA!"))


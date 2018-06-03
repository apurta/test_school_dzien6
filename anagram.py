
def anagram1(text1, text2):

    hist1 = {}
    hist2 = {}

    for char in text1.lower():
        char.isalpha():
            hist1[char] = hist1.get(char, 0) +1

    for char in text2.lower():
        char.isalpha():
            hist2[char] = hist2.get(char, 0) +1


####################

def anagram(first, second):
    hist_first = {}
    hist_second = {}

    for char in first:
        hist_first[char] = hist_first.get(char, 0) + 1

    for char in second:
        hist_second[char] = hist_second.get(char, 0) + 1

id h1 == h2 ???????????????
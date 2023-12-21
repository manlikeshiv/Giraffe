sentence = "abracadabra"

vowels = ["a", "e", "i", "o", "u"]
vowelcount = 0

for letter in sentence:
    if letter in vowels:
        vowelcount = vowelcount + 1

print (vowelcount)
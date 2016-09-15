#
# (Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
#
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvcvvc"
word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

value = (input("Enter lower for lowercase or upper for UPPERCASE: "))

if value = str("lower")):
    print(word.lower)
elif  value = str:("upper"):
    print(word.upper)
else:
    print(word)
from classifier import classify, Language
from dictionary import load_dictionary

cmd: str | None  = None

while True:
    cmd = input("Please enter a word in japanese or english.").strip()
    if len(cmd):
        break

dictionary = load_dictionary()
word_type = classify(cmd)

match = None
for entry in dictionary:
    if word_type == Language.JAPANESE:
        if cmd == entry["Vocab-Japanese"] or cmd == entry["Vocab-Kana"]:
            match = entry
            break
    elif word_type == Language.ENGLISH:
        if cmd.casefold() == entry["Vocab-English"].strip().casefold():
            match = entry
            break

if match is not None:
    if word_type == Language.JAPANESE:
        print(match["Vocab-English"])
    elif word_type == Language.ENGLISH:
        print(match["Vocab-Japanese"])

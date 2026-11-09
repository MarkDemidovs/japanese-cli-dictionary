from classifier import classify
from dictionary import load_dictionary
from lexicographer import lexicographer
import sys


if len(sys.argv) > 1:
    cmd = sys.argv[1]
else:
    while True:
        cmd: str = input("Please enter a word in japanese or english:").strip()
        if cmd:
            break

dictionary = load_dictionary()
word_type = classify(cmd)

lexicographer(dictionary, word_type, cmd)

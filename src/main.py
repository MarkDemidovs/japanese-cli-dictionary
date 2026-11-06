from classifier import classify

cmd: str | None  = None

while True:
    cmd = input("Please enter a word in japanese or english.").strip()
    if len(cmd) > 0:
        break

print(classify(cmd))

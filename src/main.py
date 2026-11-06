cmd: str | None  = None

while True:
    line = input("Please enter a word in japanese or english.").strip()
    if len(line) > 0:
        break

print(line)

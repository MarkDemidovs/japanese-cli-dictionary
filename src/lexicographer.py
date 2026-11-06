from classifier import Language


def lexicographer(
    dictionary: list[dict[str, str]], word_type: Language, cmd: str
) -> None:
    match: dict[str, str] | None = None

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
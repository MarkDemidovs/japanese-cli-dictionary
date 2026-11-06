from enum import Enum

class Language(Enum):
    ENGLISH = "english"
    JAPANESE = "japanese"
    NONE = "none"

def classify(word: str) -> Language:
    word = word.strip()

    if not word:
        return Language.NONE
    
    if word.isascii() and word.isalpha():
        return Language.ENGLISH

    for character in word:
        if is_hiragana(character) or is_katakana(character) or is_kanji(character) or character == "ー":
            continue
        else:
            return Language.NONE

    return Language.JAPANESE

def is_hiragana(character: str) -> bool:
    return 0x3040 <= ord(character) <= 0x309F

def is_katakana(character: str) -> bool:
    return 0x30A0 <= ord(character) <= 0x30FF

def is_kanji(character: str) -> bool:
    return 0x4E00 <= ord(character) <= 0x9FFF
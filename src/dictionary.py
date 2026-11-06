import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "dictionary.csv"

def load_dictionary() -> list[dict[str, str]]:
    with open(DATA_PATH, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)
import csv

with open("../data/dictionary.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
def dictionary_checker(word: str):

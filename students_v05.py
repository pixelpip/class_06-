import csv


name = input("What's your name? ")
home = input("where's your home? ")

with open("names.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
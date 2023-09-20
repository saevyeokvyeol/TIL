import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        problem = row["problem"]
        if problem in counts:
            counts[problem] += 1
        else:
            counts[problem] = 1

for problem in sorted(counts, key=lambda problem: counts[problem], reverse=True):
    print(f"{problem}: {counts[problem]}")
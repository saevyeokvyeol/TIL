import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    Ruby, C, Java, Python, JavaScript = 0, 0, 0, 0, 0
    for row in reader:
        favorite = row["language"]
        if favorite == "Ruby":
            Ruby += 1
        elif favorite == "C++":
            C += 1
        elif favorite == "Java":
            Java += 1
        elif favorite == "Python":
            Python += 1
        elif favorite == "JavaScript":
            JavaScript += 1

print(f"Ruby: {Ruby}")
print(f"C: {C}")
print(f"Java: {Java}")
print(f"Python: {Python}")
print(f"JavaScript: {JavaScript}")
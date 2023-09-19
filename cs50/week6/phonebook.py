people = {
    "Carter": "010-1111-2222",
    "David": "010-0000-9999"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
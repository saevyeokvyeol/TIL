from cs50 import get_string

s = input("Do you agree? ")

s = s.lower()
if s in ["y", "yes"]:
    print("You Agreed.")
elif s in ["n", "no"]:
    print("You not agreed.")
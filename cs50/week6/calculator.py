from cs50 import get_int

# x = get_int("x: ")
# y = get_int("y: ")
x = int(input("x: "))
y = int(input("y: "))

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)

print("----------------------")

print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)

print("----------------------")

print(f"x / y = {(x / y):.50f}")
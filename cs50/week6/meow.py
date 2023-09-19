# while loop
i = 0;
while i < 3:
    print("meow")
    i += 1

# for loop
for i in range(3):
    print("meow")

# for loop with function
def meow():
    print("meow")

for i in range(3):
    meow()

# main function with meow function
def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()

# function with parameter
def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")

main()
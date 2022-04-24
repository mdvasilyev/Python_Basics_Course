# while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

# another way to do the same thing

other_name = None

while not other_name:
    other_name = input("Enter your name: ")

print("Hello " + other_name)

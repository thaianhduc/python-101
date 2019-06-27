import random

# Define the function first. The execution is top down
def sayYourName(name):
    print(name)


message = "This is my ever first line of Python code - Hello Python"
print(message)
number = input("Hey your favorite number?\n")

sayYourName("Your favorite " + number)

letter = input("Expected a number but string\n")
number = int(letter)
"""
Your module description
"""
# STRING BASIC
myString = "This is a string."
print(myString)

print(type(myString))
print(myString + " is of the data type " + str(type(myString)))


# STRING CONCATENATION
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


# USER INPUT
name = input("What is your name? ")
print(name)


# FORMATTED OUTPUT
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name, color, animal))

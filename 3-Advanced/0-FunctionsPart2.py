# Part 0 - Functions

"""
Task - Write your own function 
    - that takes in an argument
    - and prints it out backwards
"""

def printReverse(string):
    stringReversed = string[::-1]
    print(stringReversed)

animals = ["Cat", "dog", "pig", "horse"]

for animal in animals:
    printReverse(animal)




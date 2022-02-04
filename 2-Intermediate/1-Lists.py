# Part 5- Lists

myList = ["myString", 1, 2.3, "anotherString"]

print(myList[0:-2])

"""
Task- Take in 3 inputs from a user, and add them all into a list.
        Then print out the list in reverse order
"""

myList = [
    input("please input something: "), 
    input("please input something: "), 
    input("please input something: ")
]

myList.reverse()

print(myList)

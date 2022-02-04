"""
Final Intermediate Task:
    Using what you have just learned, re-write your calculator from part 1
        to have the following functionality:
            - Allow the user to input as many numbers as they want
                - It should stop prompting for numbers when they say "stop"
            - Allow the user to specify what operation to do 
                (add, multiply, average, exit)
                - It should continue to ask what operation is to be done 
                    until the user says "exit"


Example

Input:
1
2
6
2
5
stop

Would you like to: Add, Multiply, Average, or Exit?

Input: Add

16

Input: Multiply

120

Input: Exit
"""

# =============================
#        GET THE INPUT
# =============================

# Initialize Empty List
from unittest import result

from numpy import average


myNumbers = []

# Initialize user input
userInput = ""

# While userinput isn't stop, add numbers to the list
while userInput != "stop":
    userInput = input("Enter a number: ")
    if(userInput != "stop"):
        myNumbers.append(int(userInput))


# =============================
#        DO THE MATH
# =============================

# Initialize user input
userInput = ""

# While userinput isn't stop, add numbers to the list
while userInput != "exit":

    userInput = input("Would you like to: add, multiply, average, or exit? ").lower()

    if userInput == "add":
        summation = sum(myNumbers)
        
        print(f"The sum is {summation}")

    elif userInput == "multiply":
        result = 1
        for number in myNumbers:
            result = result * number

        print(f"The product is {result}")

    elif userInput == "average":
        summation = sum(myNumbers)
        average = summation / len(myNumbers)

        print(f"The average is {average}")

    elif userInput == "exit":
        print("Goodbye!")
        exit()

    else:
        print(f"Unknown input: {userInput}")
"""
Final Beginner Task:
    Take the users input to get four numbers
    Print out the 4 numbers the user entered in one line, 
        with a sentence to remind them what they entered
    Then calculate the average, sum, and product of these numbers,
        and print out these values with an 'fstring'

Example:

Enter your 4 numbers
Number 1: 8
Number 2: 12
Number 3: 3
Number 4: 19

You entered: 8 12 3 19
The Sum is: 42
The Average is: 10.5
The Product is: 5472
"""


print("Please Enter Your 4 Numbers")

# Take in the user input
Number1 = int(input("Number 1: "))
Number2 = int(input("Number 2: "))
Number3 = int(input("Number 3: "))
Number4 = int(input("Number 4: "))

# Remind the user
print(f"You entered: {Number1}, {Number2}, {Number3}, {Number4}")

# Do all the math
numSum = Number1 + Number2 + Number3 + Number4
avg = numSum / 4
product =  Number1 * Number2 * Number3 * Number4

# Show the results
print(f"The sum is: {numSum}")
print(f"The average is: {avg}")
print(f"The product is: {product}")
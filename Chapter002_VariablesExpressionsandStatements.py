# Values- the data that are to be stored in the variables
print("Values:")
# Print statement
print("Hello World!!")
# For getting type of the data
print(type("Hello World!!"))
# Print statement
print(17)
# For getting type of the data
print(type(17))
# Print statement
print(3.5)
# For getting type of data
print(type(3.5))
# Same for others too

# Variables- The container thar are used to store the data
print("Variables:")
# Storing integer
n=17
print("Value stored in n: ",n)
# Storing string
message="I am Vikas Shanabhog"
print(message)
print()

# Operators- The smbols that are used to perform the computation
print("Operators:")
# Operands- The values on which the operations are performed
# Addition
sum=2+2
print("Addition: ",sum)
# Subtraction
difference=4-2
print("Substraciton: ",difference)
# Multiplication
product=2*2
print("Multiplication: ",product)
# Division
quotient=4//2
print("Quotient: ",quotient)
remainder=3%2  # Modulus
print("Remainder: ",remainder)
# Exponentiation
expo=2**4
print("Exponentiation: ",expo)
print()

# Expressions- Combination of values, variables and operators
print("Expressions:")
x=1
x=x+17
print("Sum of the value present in x and 17 is: ",x)
print()

# Order of Precedence
print("Order of Precedence:")
print("1. Paranthesis")
print("2. Exponentiation")
print("3. Multiplication and Division")
print("Operators with same precedence are evaluated from left to right")
print()

# String Operations
print("String Operations:")
# + is for concatenation
statement1="Hey I am"
statement2="Vikas"
resultantstatement=statement1+" "+statement2
print("Concatenation of two strings: ",resultantstatement)
# * is for number of times the string is repetited 
first="Test "
second=3
resultantstatement1=first * second
print("Number of times the string is repeated: ",resultantstatement1)
print()

# Getting input from the user
# Getting name as an input from the user
print("Getting input from the user:")
name=input("What is your name? \n")
print("My name is: ",name)
# Getting age as the input from the user
prompt="What is your age? \n"
age=int(input(prompt)) # When the user tries to give string data it gives error
print("My age is: ",age)
print(type(age))
# Getting float as the input from the user
hours=float(input("Enter the hours: \n"))
rate=float(input("Enter the rate: \n"))
pay=hours*rate
print("Payment: ",pay)

# Arithmatic operators
# + Addition
# - Substraction
# * Multiplication
# / or // Division
# % Modulus

# Comparison Operators
# < Less than 
# <= Less than or equal to
# > Greater than
# >= Greater than or equal to 
# == Equal to 
# != Not equal to

# Logical Operators
# and: If both the statements are true
# or: If one of the statements is true
# not: Opposite of the given statemement or value
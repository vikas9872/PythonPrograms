# Functions: Sequence of statements that perform computation

# Function without parameter without return type
print("Function without parameter without return type: ")
def thing():
    print("Zig")
thing()
print()

# Function without patameter with return type
print("Function without parameter with return type: ")
def addition():
    a=20
    b=30
    add=a+b
    return add
sum=addition()
print("Addition of two numbers: ",sum)
print()

# Function with parameter without return type
print("Function with parameter without return type: ")
def substraction(a,b):
    difference=a-b
    print("Difference of two numbers: ",difference)   
num1=int(input("Enter the value of num1: \n"))
num2=int(input("Enter the value of num2: \n"))
substraction(num1,num2)
print()

# Function with parameter with return type
print("Function with parameter with return type: ")
def multiplication(c,d):
    mul=c*d
    return mul
num3=int(input("Enter the value of num3: \n"))
num4=int(input("Enter the value of num4: \n"))
product=multiplication(num3,num4)
print("Product of two numbers: ",product)
print()

# Built in functions
print("Built in functions: ")
prompt="Enter the value of num5: \n"
prompt1="Enter the value of num6: \n"
num5=int(input(prompt))
num6=int(input(prompt1))
maximum=max(num5,num6)
minimum=min(num5,num6)
maximumType=type(maximum)
minimumType=type(minimum)
print("Maximum of two numbers: ",maximum)
print("Minimum of two numbers: ",minimum)
print("Type of maximum: ",maximumType)
print("Type of minimum: ",minimumType)
print()

# Type Conversions
print("Type Conversions: ")
a="10"
typeofa=type(a)
print("Value of a: ",a)
print("Type of a before: ",typeofa)
newa=int(a)
typeofnewa=type(newa)
print("Value of a after changing to int: ",newa)
print("Type of a after changing to int: ",typeofnewa)
verynewa=float(a)
typeofverynewa=type(verynewa)
print("Value of a after changing to float: ",verynewa)
print("Type of a after changing to float: ",typeofverynewa)
# Note: Same for other datatypes
print()

# Math Functions
print("Math Functions: ")
import math
radius=int(input("Enter the radius: \n"))
areaofcircle=(math.pi*radius*radius)
print("Area of circle: ",areaofcircle)
prompt2="Enter the number to find the squareroot: \n"
number=int(input(prompt2))
squareroot=math.sqrt(number)
print("Square root of the nummber: ",squareroot)
print()

# Random functions
print("Random Functions: ")
import random
# Random includes both the parameters i.e may print low and high values provided
random1=random.randint(5,10)
print("Selected random integer: ",random1)
# Selecting one option from the given options
options=[10,20,30]
option=random.choice(options)
print("Selected option: ",option)

# Fuction inside function
def lyrics():
    print("This is lyrics")

def song():
    lyrics()
    print("This is song")
song()
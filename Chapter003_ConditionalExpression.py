# Conditional Statement

# if statement
print("If Statement")
prompt="What is the age? \n"
age=int(input(prompt))
if age < 18:
    print("Person is not eligible to vote")
print()

# if else statement
print("If-else Statement")
prompt1="What is your age? \n"
age1=int(input(prompt1))
if age1 < 18:
    print("Person is not eligible to vote")
else:
    print("Person is eligible to vote")
print()

# elif statement
print("El-if Statement")
prompt2="What is the price? \n"
price=int(input(prompt2))
if price < 100: 
    print("Price is less than 100")
elif price == 100:
    print("Price is equal to 100")
else:
    print("Price is greater than 100")
print()

# Nested conditions
print("Nested Conditions")
x=int(input("Enter the value of x: \n"))
y=int(input("Eneter the value of y: \n"))
if x==y:
    print("x and y are equal")
else:
    if x>y:
        print("x is greater than y")
    else:
        print("x is less than y")

# try and except
print("Try and except")
a=input("Enter the value of a: \n")
b=input("Enter the value of b: \n")
try:
    num1=int(a)
    num2=int(b)
except:
    print("Error, please enter the numeric input")
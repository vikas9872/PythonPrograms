print("Exercise 2.1")
# Write a program that uses input to propt a user fot their name and then welcomes them
prompt="Enter the name: \n"
name=input(prompt)
print("Hello ",name)
print()

print("Exercise 2.2")
# Write a program to prompt the user for hours and rate per hour to compute the gross pay
hours=float(input("Enter the hours: \n"))
rate=float(input("Enter the rate: \n"))
pay=hours*rate
print("Payment: ",pay)
print()

print("Exercise 2.3")
# Assume width=12.0 and height=17. Perform the following expressions
width=12.0
height=17
quotient1=width//2
print("Quotient1: ",quotient1)
quotient2=width/2.0
print("Quotient2: ",quotient2)
quotient3=height/3
print("Quotient3: ",quotient3)
result=1+2*5
print("Result: ",result)
print()
 
print("Exercise 2.4")
# Convert Celcius to Farenheit
celcius=int(input("Enter the temperature in celcius: \n"))
farenheit=9/5*celcius+32
print("Temperature in farenheit: ",farenheit)
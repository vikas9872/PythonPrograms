print("Exercise 3.1")
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours=float(input("Enter the hours: \n"))
rate=float(input("Enter the rate: \n"))
if hours > 40:
    pay=(40*rate)+((hours-40)*rate*1.5)
else:
    pay=hours*rate
print("Payment: ",pay)
print()

print("Exercise 3.2")
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully 
# by printing a message and exiting the program.
h=input("Enter hours: \n")
r=input("Enter rate: \n")
try:
    hrs=float(h)
    rt=float(r)
except:
    print("Error, please enter the numerical value")
print()

print("Exercise 3.3")
#  Write a program to prompt for a score between 0.0 and 1.0. If the
#  score is out of range, print an error message. If the score is between 0.0 and 1.0,
#  print a grade using the following table:
#  Score   Grade
#  >= 0.9    A
#  >= 0.8    B
#  >= 0.7    C
#  >= 0.6    D
#  < 0.6     F
prompt="Enter the score between 0.0 and 1.0: \n"
s=input(prompt)
try:
    score=float(s)
    if score < 0 or score > 1:
        x="Bad score"
    elif score >= 0.9:
        x="A"
    elif score >= 0.8:
        x="B"
    elif score >= 0.7:
        x="C"
    elif score >= 0.6:
        x="D"
    elif score < 0.6:
        x="E"
    print(x)
except:
    print("Bad score")
print("Exercise 4.1")
# 1. Predict the output
def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()
print()

print("Exercise 4.3")
# 2. Rewrite the pay computation program
def computancy(hours, rate):
    if hours > 40:
        pay=(40*rate)+(1.5*(hours-40)*rate)
        return pay
    else:
        pay=hours*rate
        return pay
h=float(input("Enter the hours: \n"))
r=float(input("Enter the rate: \n"))
payment=computancy(h,r)
print(f"Total wage: {payment}")
print()

print("Exercise 4.3")
# 3. Rewrite the grade program using function called computergrade that takes score as a parameter and returns a good grade
def computergrade(score):
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
        return x
    except:
        return "Bad Score"
prompt="Enter the score between 0.0 and 1.0: \n"
s=input(prompt)
grade=computergrade(s)
print(f"Grade: {grade}")
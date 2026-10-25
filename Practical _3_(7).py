# Question 7: Simple Calculator using Conditions

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator! please enter +, -, *, or /.")

# Question 8: Discount Eligibility System

amount = float(input("Enter purchase amount:"))
if amount >= 2000:
    discount = 0.20
elif amount >= 1000:
  

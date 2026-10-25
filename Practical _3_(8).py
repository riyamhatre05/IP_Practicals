# Question 8: Discount Eligibility System (Continued)

amount = float(input("Enter purchase amount :"))
if amount >= 2000:
    discount = amount * 20 / 100
elif amount >= 1000:
    discount = amount * 10 / 100
else:
    discount = 0

Final_amount = amount - discount
print("Discount =", discount)
print("Final amount =", Final_amount)

# Question 9: Triangle Type Identifier
side1 = float(input("Enter first side:"))

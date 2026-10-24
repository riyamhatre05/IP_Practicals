km = float(input("Enter kilometers: "))
celsius = float(input("Enter temperature in celsius: "))
rupees = float(input("Enter Rupees: "))

meters = km * 1000
Fahrenheit = (celsius * 9 / 5) + 32
dollars = rupees / 85  # Example conversion rate

print("Meters =", meters)
print("Fahrenheit =", Fahrenheit)
print("US Dollars =", round(dollars, 2))

# Question 4: Factorial Calculation (using for loop)

num = int(input("Enter a number :"))
factorial = 1

# calculate factorial
for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)

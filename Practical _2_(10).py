# Division by zero
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a / b)
except zeroDivisionError:
    print("Error: Division by zero is not allowed.")

# string + Number
try:
    s = "10"
    n = 5
    print(s + n)
except TypeError:
    print("Error: cannot and string and integer.")

# correct way
print(int(s) + n)

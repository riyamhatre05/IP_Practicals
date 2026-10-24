# Method 1: Using third variable

a = 10
b = 20

print("Before swap (method 1):", a, b)

temp = a
a = b
b = temp

print("After swap (method 1):", a, b)


# Method 2: Tuple unpacking

x = 100
y = 200

print("\nBefore swap (method 2):", x, y)

x, y = y, x

print("After swap (method 2):", x, y)

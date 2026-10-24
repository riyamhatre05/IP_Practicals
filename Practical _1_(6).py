# Implicit Type Conversion

a = 10       # int
b = 2.5      # float

result = a + b

print("Implicit Conversion (int + float):", result)
print("Type:", type(result))


# Explicit Type Conversion (Correct Usage)

x = 10
y = "5"

y = int(y)   # Converting string to integer

result2 = x + y

print("\nExplicit Conversion (int + str converted to int):", result2)


# Error Example: int + string

p = 10
q = "Hello"

# This will cause an error
# print(p + q)

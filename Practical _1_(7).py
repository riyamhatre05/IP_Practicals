# Same value assigned to two variables

a = 10
b = 10

print("a id:", id(a))
print("b id:", id(b))


# Modifying one variable

a = 20

print("\nAfter modifying a:")
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))

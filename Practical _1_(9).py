# Taking two inputs

a = input("Enter first value: ")
b = input("Enter second value: ")

# Checking if both are numeric
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    result = a + b

    print("\nBoth inputs are numeric.")
    print("Sum:", result)

elif a.isalpha() and b.isalpha():
    result = a + b

    print("\nBoth inputs are strings.")
    print("Concatenation:", result)

else:
    print("\nInvalid input type. Cannot perform operation.")

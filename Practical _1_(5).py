age = input("Enter your age: ")
marks = input("Enter your marks: ")

# Display original types
print("\nBefore conversion:")
print("Age:", age, "Type:", type(age))
print("Marks:", marks, "Type:", type(marks))

# Type conversion (casting)
age = int(age)
marks = float(marks)

# Performing arithmetic operations
future_age = age + 5
total_marks = marks + 10

print("\nAfter conversion:")
print("Age (int):", age)
print("Marks (float):", marks)

print("\nArithmetic operations:")
print("Age after 5 years:", future_age)
print("Marks after bonus:", total_marks)

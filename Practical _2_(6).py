import math

# Input rectangle dimensions
length = float(input("Enter Rectangle Length: "))
breadth = float(input("Enter Rectangle Breadth: "))

# Calculate rectangle area and perimeter
area_rect = length * breadth
perimeter_rect = 2 * (length + breadth)

# Input circle radius
radius = float(input("Enter Circle Radius: "))

# Calculate circle area and circumference
area_circle = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display results
print("\nRectangle")
print("Area:", area_rect)
print("Perimeter:", perimeter_rect)

print("\nCircle")
print("Area:", area_circle)
print("Circumference:", circumference)

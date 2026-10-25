# Question 10: Menu-Driven Program

print("MENU")
print("1. check Even / odd")
print("2. Find Largest")
print("3. Grade system")

choice = int(input("Enter your choice:"))

if choice == 1:
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("Even number")
    else:
        print("odd number")
elif choice == 2:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter Third number:"))
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print("Largest number =", largest)
elif choice == 3:
    marks = float(input("Enter your marks:"))
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade c")
    elif marks >= 50:
      

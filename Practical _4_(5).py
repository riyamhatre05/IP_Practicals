# Question 5: Multiplication Table Generator

num = int(input("Enter a number:"))
# print multiplication table
print("\nMultiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
  

# Question 7: Count Digits, Even and Odd

num = int(input("Enter a number:"))
total = 0
even = 0
odd = 0
while num > 0:
    digit = num % 10
    total += 1
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print("Total digits :", total)
print("Even digits :", even)
print("odd digits :", odd)

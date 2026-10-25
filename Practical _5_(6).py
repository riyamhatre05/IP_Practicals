# Question 6: Skip Negative Numbers

# Input list of numbers
numbers = [10, -5, 20, -3, 15, -8, 25]
# print only positive numbers
print("positive numbers:")
for num in numbers:
    if num < 0:
        continue
    print(num)
  

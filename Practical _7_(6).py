# Question 6: Removing Elements from List (Handling missing elements)

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers.remove(30)
numbers.pop(1)
print("Updated list:", numbers)

try:
    numbers.remove(100)
except ValueError:
    print("Element not present in the list")
  

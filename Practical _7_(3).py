# Question 3: Slicing Lists and Tuples

# Compare results for list and tuple
numbers_list = [10, 20, 30, 40, 50]
numbers_tuple = (10, 20, 30, 40, 50)

print("list:")
print("First 3 elements:", numbers_list[:3])
print("Last 2 elements:", numbers_list[-2:])
print("Alternate elements:", numbers_list[::2])

print("\nTuple:")
print("First 3 elements:", numbers_tuple[:3])
print("Last 2 elements:", numbers_tuple[-2:])
print("Alternate elements:", numbers_tuple[::2])

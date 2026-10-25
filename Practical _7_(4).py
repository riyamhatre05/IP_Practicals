# Question 4: List Mutability vs Tuple Immutability

my_list = [10, 20, 30]
print("Original list:", my_list)
my_list[1] = 50
print("Modified list:", my_list)

my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)
# Trying to modify a tuple results in a TypeError (immutability)
my_tuple[1] = 50

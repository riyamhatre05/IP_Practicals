# Question 10: Reshaping Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(arr)

matrix = arr.reshape(2, 3)
print("\nReshaped array:")
print(matrix)

matrix2 = arr.reshape(3, 2)
print("\nAnother shape:")
print(matrix2)

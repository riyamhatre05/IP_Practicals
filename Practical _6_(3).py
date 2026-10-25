# Question 3: Sum of Rows and Columns

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Row sums:")
for i in range(len(matrix)):
    total = 0
    for j in range(len(matrix[i])):
        total += matrix[i][j]
    print("Row", i + 1, "=", total)

# sum of each column
print("\ncolumn sums:")
for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)): 
  

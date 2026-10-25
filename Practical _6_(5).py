# Question 5: Transpose of a Matrix

matrix = [[1, 2, 3], [4, 5, 6]]

print("Original matrix:")
for row in matrix:
    print(row)

transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
  

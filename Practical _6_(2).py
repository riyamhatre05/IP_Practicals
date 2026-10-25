# Question 2: Matrix Traversal[span_0](start_span)[span_0](end_span)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]  #[span_1](start_span)[span_1](end_span)

print("Row - wise:")  #[span_2](start_span)[span_2](end_span)
for i in range(len(matrix)):  #[span_3](start_span)[span_3](end_span)
    for j in range(len(matrix[i])):  #[span_4](start_span)[span_4](end_span)
        print(matrix[i][j], end=" ")  #[span_5](start_span)[span_5](end_span)
print()  #[span_6](start_span)[span_6](end_span)

print("\ncolumn - wise:")  #[span_7](start_span)[span_7](end_span)
for j in range(len(matrix[0])):  #[span_8](start_span)[span_8](end_span)
    for i in range(len(matrix)):  #[span_9](start_span)[span_9](end_span)
        print(matrix[i][j], end=" ")  #[span_10](start_span)[span_10](end_span)
print()  #[span_11](start_span)[span_11](end_span)

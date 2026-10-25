# Question 4: Matrix Addition[span_0](start_span)[span_0](end_span)

matrix1 = [
    [1, 2, 3],  #[span_1](start_span)[span_1](end_span)
    [4, 5, 6],  #[span_2](start_span)[span_2](end_span)
]  #[span_3](start_span)[span_3](end_span)

matrix2 = [
    [7, 8, 9],  #[span_4](start_span)[span_4](end_span)
    [10, 11, 12],  #[span_5](start_span)[span_5](end_span)
]  #[span_6](start_span)[span_6](end_span)

result = []  #[span_7](start_span)[span_7](end_span)
for i in range(len(matrix1)):  #[span_8](start_span)[span_8](end_span)
    row = []  #[span_9](start_span)[span_9](end_span)
    for j in range(len(matrix1[0])):  #[span_10](start_span)[span_10](end_span)
        row.append(matrix1[i][j] + matrix2[i][j])  #[span_11](start_span)[span_11](end_span)
    result.append(row)  #[span_12](start_span)[span_12](end_span)

print("Result Matrix:")  #[span_13](start_span)[span_13](end_span)
for row in result:  #[span_14](start_span)[span_14](end_span)
    print(row)  #[span_15](start_span)[span_15](end_span)

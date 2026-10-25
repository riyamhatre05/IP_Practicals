# Question 11: Iterating Through Lists and Tuples[span_0](start_span)[span_0](end_span)

numbers_list = [10, 20, 30, 40, 50][span_1](start_span)[span_1](end_span)
numbers_tuple = (10, 20, 30, 40, 50)[span_2](start_span)[span_2](end_span)

print("Element of list :")[span_3](start_span)[span_3](end_span)
for number in numbers_list:[span_4](start_span)[span_4](end_span)
    print(number)[span_5](start_span)[span_5](end_span)

total_list = 0[span_6](start_span)[span_6](end_span)
for number in numbers_list:[span_7](start_span)[span_7](end_span)
    total_list = total_list + number[span_8](start_span)[span_8](end_span)
print("sum of list :", total_list)[span_9](start_span)[span_9](end_span)

print("Elements of tuple :")[span_10](start_span)[span_10](end_span)
for number in numbers_tuple:[span_11](start_span)[span_11](end_span)
    print(number)[span_12](start_span)[span_12](end_span)

total_tuple = 0[span_13](start_span)[span_13](end_span)
for number in numbers_tuple:[span_14](start_span)[span_14](end_span)
    total_tuple = total_tuple + number[span_15](start_span)[span_15](end_span)
print("sum of tuple :", total_tuple)[span_16](start_span)[span_16](end_span)
print("Iteration is similar for both list and tuple.")[span_17](start_span)[span_17](end_span)

# Question 8: Prime Number Checker[span_0](start_span)[span_0](end_span)

print("Prime numbers between 1 and 100 are:")[span_1](start_span)[span_1](end_span)
for num in range(2, 101):[span_2](start_span)[span_2](end_span)
    for i in range(2, int(num ** 0.5) + 1):[span_3](start_span)[span_3](end_span)
        if num % i == 0:[span_4](start_span)[span_4](end_span)
            break  # Not prime, exit inner loop[span_5](start_span)[span_5](end_span)
    else:[span_6](start_span)[span_6](end_span)
        print(num, end=" ")[span_7](start_span)[span_7](end_span)

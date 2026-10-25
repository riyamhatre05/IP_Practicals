# Question 7: Sum of Valid Inputs Only[span_0](start_span)[span_0](end_span)

total = 0[span_1](start_span)[span_1](end_span)
while True:[span_2](start_span)[span_2](end_span)
    num = int(input("Enter a number:"))[span_3](start_span)[span_3](end_span)
    if num == 0:[span_4](start_span)[span_4](end_span)
        break[span_5](start_span)[span_5](end_span)
    if num < 0:[span_6](start_span)[span_6](end_span)
        continue[span_7](start_span)[span_7](end_span)
    total = total + num[span_8](start_span)[span_8](end_span)

print("Sum of valid inputs:", total)[span_9](start_span)[span_9](end_span)

# Question 5: First Divisible Number Finder[span_0](start_span)[span_0](end_span)

# Input a number[span_1](start_span)[span_1](end_span)
n = int(input("Enter a number:"))[span_2](start_span)[span_2](end_span)
# Find the first number divisible by n[span_3](start_span)[span_3](end_span)
for i in range(1, 101):[span_4](start_span)[span_4](end_span)
    if i % n == 0:[span_5](start_span)[span_5](end_span)
        print("First number divisible by", n, "is", i)[span_6](start_span)[span_6](end_span)
        break

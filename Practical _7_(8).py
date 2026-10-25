# Question 8: Tuple Methods - count() and index()[span_8](start_span)[span_8](end_span)

numbers = (10, 20, 10, 30, 10, 40)[span_9](start_span)[span_9](end_span)
print("Count of 10:", numbers.count(10))[span_10](start_span)[span_10](end_span)
print("Index of 30:", numbers.index(30))[span_11](start_span)[span_11](end_span)

try:[span_12](start_span)[span_12](end_span)
    print("Index of 50:", numbers.index(50))[span_13](start_span)[span_13](end_span)
except ValueError:[span_14](start_span)[span_14](end_span)
    print("Element 50 is not present in the tuple")[span_15](start_span)[span_15](end_span)

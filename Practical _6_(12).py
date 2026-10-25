# Question 12: Real-World Dataset Analysis[span_0](start_span)[span_0](end_span)

import numpy as np[span_1](start_span)[span_1](end_span)

marks = np.array(
    [[80, 75, 90], [65, 70, 60], [90, 85, 95], [55, 60, 50], [75, 80, 70]]
)[span_2](start_span)[span_2](end_span)

print("Marks Dataset:")[span_3](start_span)[span_3](end_span)
print(marks)[span_4](start_span)[span_4](end_span)
average = np.mean(marks, axis=1)[span_5](start_span)[span_5](end_span)
print("\nAverage marks of each student:")[span_6](start_span)[span_6](end_span)
for i in range(len(average)):[span_7](start_span)[span_7](end_span)
    print("student", i + 1, ":", average[i])[span_8](start_span)[span_8](end_span)
print("\nHighest mark:", np.max(marks))[span_9](start_span)[span_9](end_span)
print("lowest mark:", np.min(marks))[span_10](start_span)[span_10](end_span)
print("Overall average:", np.mean(marks))[span_11](start_span)[span_11](end_span)

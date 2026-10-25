# Question 7: Array Indexing and Slicing[span_0](start_span)[span_0](end_span)

import numpy as np[span_1](start_span)[span_1](end_span)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])[span_2](start_span)[span_2](end_span)
print("Array:")[span_3](start_span)[span_3](end_span)
print(arr)[span_4](start_span)[span_4](end_span)

print("\nspecific element:", arr[1, 2])[span_5](start_span)[span_5](end_span)
# Entire row[span_6](start_span)[span_6](end_span)
print("second row:", arr[1, :])[span_7](start_span)[span_7](end_span)
# Entire column[span_8](start_span)[span_8](end_span)
print("second column:", arr[:, 1])[span_9](start_span)[span_9](end_span)
# Slicing[span_10](start_span)[span_10](end_span)
print("First two rows:")[span_11](start_span)[span_11](end_span)
print(arr[0:2, :])[span_12](start_span)[span_12](end_span)

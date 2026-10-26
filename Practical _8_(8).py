# Input a string[span_0](start_span)[span_0](end_span)
text = input("Enter a string:")[span_1](start_span)[span_1](end_span)

# Initialize an empty dictionary[span_2](start_span)[span_2](end_span)
frequency = {}[span_3](start_span)[span_3](end_span)

# Count the frequency of each character[span_4](start_span)[span_4](end_span)
for ch in text:[span_5](start_span)[span_5](end_span)
    if ch in frequency:[span_6](start_span)[span_6](end_span)
        frequency[ch] += 1[span_7](start_span)[span_7](end_span)
    else:[span_8](start_span)[span_8](end_span)
        frequency[ch] = 1[span_9](start_span)[span_9](end_span)

# Print the final frequency dictionary[span_10](start_span)[span_10](end_span)
print(frequency)[span_11](start_span)[span_11](end_span)

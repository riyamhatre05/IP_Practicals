# Create first dictionary[span_0](start_span)[span_0](end_span)
dict1 = {
    "A": 10,
    "B": 20
}

# Create second dictionary[span_1](start_span)[span_1](end_span)
dict2 = {
    "B": 50,
    "C": 30
}

# Merge them using update() to observe key overwrite behavior[span_2](start_span)[span_2](end_span)
dict1.update(dict2)  #[span_3](start_span)[span_3](end_span)
print(dict1)         #[span_4](start_span)[span_4](end_span)

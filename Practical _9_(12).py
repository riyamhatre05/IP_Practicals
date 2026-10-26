# Function to input marks for 3 subjects
def marks():
    return [int(input("Marks:")) for i in range(3)]  #[span_0](start_span)[span_0](end_span)

# Function to calculate total, percentage, grade, and display results
def result(m):
    t = sum(m)  #[span_1](start_span)[span_1](end_span)
    p = t / 3  #[span_2](start_span)[span_2](end_span)
    g = "A" if p >= 75 else "B" if p >= 60 else "C" if p >= 40 else "F"  #[span_3](start_span)[span_3](end_span)
    print("total:", t)  #[span_4](start_span)[span_4](end_span)
    print("Percentage:", p)  #[span_5](start_span)[span_5](end_span)
    print("Grade:", g)  #[span_6](start_span)[span_6](end_span)

# Combine all functions and execute the program
result(marks())  #[span_7](start_span)[span_7](end_span)

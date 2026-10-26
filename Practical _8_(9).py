# Creating a dictionary of students with nested details[span_0](start_span)[span_0](end_span)
students = {
    "101": {
        "Name": "Rahul",
        "Marks": 85
    },
    "102": {
        "Name": "Priya"
    }
}

# Accessing nested values[span_1](start_span)[span_1](end_span)
print(students["101"]["Name"])

# Modifying nested data[span_2](start_span)[span_2](end_span)
students["102"]["Marks"] = 85
print(students)

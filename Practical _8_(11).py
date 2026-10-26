# Create the student dictionary
student = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78
}  #

# Sort and display by keys
print("sorted by keys:")  #
for key in sorted(student):  #
    print(key, student[key])  #

# Sort and display by values
print("\nSorted by values:")  #
for key, value in sorted(student.items(), key=lambda x: x[1]):  #
    print(key, value)  #

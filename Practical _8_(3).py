print(student.get("Name"))
print(student.get("city"))
print(student.get("city", "Not available"))

# Question 4: Adding and Updating Elements
student["Marks"] = 85  # add
student["Age"] = 21    # update
print(student)

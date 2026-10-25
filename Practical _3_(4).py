# Question 4: Nested If Statements

age = int(input("Enter your age:"))  #
nationality = input("Enter your nationality:")  #
if age >= 18:  #
    if nationality.lower() == "indian":  #
        print("Eligible to vote.")  #
    else:  #
        print("Not Eligible to vote (only indian citizens can vote).")  #
else:  #
    print("Not Eligible to vote (Age must be 18 or above.)")  #

# Question 8: Password Retry System

# set the correct password
correct_Password = "Riya05"
# Allow 3 attempts
for i in range(1, 4):
    password = input("Enter password:")
    if password == correct_Password:
        print("Login Successful!")
        break
    else:
        print("Incorrect password.")
else:
    print("
          

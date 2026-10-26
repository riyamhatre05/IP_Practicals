# Use global keyword
x = 10

def change():
    global x
    x = 20
    print("inside:", x)

print("Before:", x)  #
change()             #
print("After:", x)   #

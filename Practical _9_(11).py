# Define functions for addition, prime check, and factorial
def add(a, b):
    return a + b  #

def prime(n):
    return n > 1 and all(n % i for i in range(2, n))  #

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)  #

# Menu options and user choice
print("1. Add 2. prime 3. factorial")  #
c = int(input("choice:"))  #

if c == 1:
    a = int(input("A:"))  #
    b = int(input("B:"))  #
    print(add(a, b))  #
elif c == 2:
    n = int(input("Number:"))  #
    print("prime" if prime(n) else "Not Prime")  #
elif c == 3:
    n = int(input("Number:"))  #
    print(fact(n))  #

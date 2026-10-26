# Generate Fibonacci sequence using recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  #

n = int(input("Enter terms:"))  #
for i in range(n):
    print(fib(i), end=" ")  #

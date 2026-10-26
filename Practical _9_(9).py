def input_data():
    n = int(input("Enter number:"))
    return n

def process(n):
    return n * n

def Output(n):
    print("Square:", n)

def main():
    n = input_data()    #
    result = process(n) #
    Output(result)      #

main()                  #

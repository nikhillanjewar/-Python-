# Fibonacci Sequence using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a number here:"))
if n <= 0:
    print("Input should be a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))
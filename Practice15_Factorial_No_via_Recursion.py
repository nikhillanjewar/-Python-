# factorial of a Number - By recursion


def fact(a):
    if a==0:
        return 1
    else:
        return ((a)*fact(a-1))
num = int(input("Enter a Number Here:"))
result = fact(num)
print("The Factorial of a Number is: ", result)

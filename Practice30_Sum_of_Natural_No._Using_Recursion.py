# Sum of Natural Number Using Recusrion/ Natural Numbers means Positive Integrers

def sum_of_natural_number(n):
    if n <= 1:
        return n
    else:
        return (n) + sum_of_natural_number(n-1)

n =int(input("Enter a Number here:"))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("The sum of natural number is",sum_of_natural_number(n))



# FIND & CALCULATE SQUARE ROOT

# using operator/exponentiation
# step-1(direct assigning a number)
num1 =64
# exponention operator
sr = num1**(1/2)
print("The square root of the Given Number is",sr)


# step-2 (from user input)
num2 = int(input("Enter a number here:"))
Sr = num2**(1/2)
print("The square root of the Given Number is",Sr)



# using math module
import math
num3 = int(input("Enter a number here:"))
sr2 = math.sqrt(num3)
print("The Square root of the Number is",sr2)
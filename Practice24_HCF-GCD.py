# Highest common Factor and Greatest Common Divisor of two numbers

def findHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
            # x=12
            # y=18
print("The HCF of the given two number is",findHCF(12, 18))  # Output: 6

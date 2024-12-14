# Find the Factorial of a Number - 5! = 5*4*3*2*1

num = int(input("Enter the Number:"))
fact = 1

if num<0:
    print("The Factorial of 0 does not exist")
if num==0:
    print("Factorial of 0 is", 1)
if num>0:
    for i in range(1, num+1):
        fact = fact*i
print("The Factorial of the Given Number is", fact)
    


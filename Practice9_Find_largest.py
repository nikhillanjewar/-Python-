# FIND THE LARGEST AMONG THREE NUMBERS

num1 = int(input("Enter a First Number:"))
num2 = int(input("Enter a Second Number:"))
num3 = int(input("Enter a Third Number:"))

if(num1>num2) and (num1>num3):
    print(num1, "First Number is Largest")

elif(num2>num1) and (num2>num3):
        print(num2, "Second Number is Largest")

else:
        print(num3, "Third Number is Largest")

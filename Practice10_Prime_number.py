# CHECK THE PRIME NUMBER

num = int(input("Enter the Number:"))

if num <= 1:
    print("It is not a prime Number")

if num>1:
    for i in range(2, num):
        if num % i == 0:
            print("Number is Not a prime Number")
            break
    else:
        print("Number is prime Number")

# Armstrong Number - 

# 153 = (1*1*1) + (5*5*5) + (3*3*3) = 1+125+27 =153 (this is technique of armstrong number)

num = int(input("Enter a only three digit number:"))
sum = 0
temp = num
while temp>0:
    digit = temp%10

    # change as perreuirement
    cube = digit**3
    sum = sum+cube
    temp//=10

if sum == num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")


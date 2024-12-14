# Creating simple calculator
print("~~~~Mini Calculator~~~~")

num1 = float(input("Enter you First Number: "))
num2 = float(input("Enter you Second Number: "))

# list of operation (+,-,*,/)
print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division")
choice = int(input("Enter your choice from 1-4: "))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
else:
    print(num1/num2)

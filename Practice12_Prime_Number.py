# PRINT ALL PRIME NUMBERS IN AN INTERVAL-   

lower_value = int(input("Enter the Lower Value:"))
higher_value = int(input("Enter the higher Value:"))

for num in range (lower_value, higher_value+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:  
                break
            else:
                print(num)

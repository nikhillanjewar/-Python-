# TO CHECK WHETHER THE LEAP YEAR 
 
Year = int(input("Enter a Year:"))


if(Year % 400 == 0) and (Year % 100 == 0):
    print(Year, "is a leap year")

elif(Year % 4 == 0) and (Year % 100 != 0):
    print(Year, "is a leap year")

else:
    print(Year, "is not a Leap Year")
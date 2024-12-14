# to print the Display the calendar of the Month
import calendar

year = int(input("Enter a Year:"))
month = int(input("Enter a Month:"))
calendar = calendar.month(year,month)
print(calendar)
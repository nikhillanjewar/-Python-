# find Numbers DIvisible by Another Number

# by using for loop and conditional statements
print("The Numbers divisible by 13 are:")
for i in range(1,132):
    if i % 13 == 0:
        print(i)



# byusing lambda function and filter function
print("\nThe Numbers divisible by 13 are:")
print(*list(filter(lambda x: x % 13 == 0, range(1,132))))


# Display the Multiplication Table

# by using for loop
n = int(input("Enter a number here:"))
for i in range(1,11):
    print(n, "x", i, "=", n*i)


# by using while loop
n=7
i=1
while i<=10:
    print(n,"x", i, "=", n*i)
    i+=1
